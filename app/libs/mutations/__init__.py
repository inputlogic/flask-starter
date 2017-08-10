from flask_login import current_user
from mongoengine import ValidationError
from mongoengine.errors import NotUniqueError

from app.libs.errors import InvalidData, ServiceUnavailable
from app.models.playlist_video import PlaylistVideo
from app.libs import permissions, hasher, vhx, metrics
from app.models.user import User


def create(model, request, args=None, force_args={}):
    '''
    Create a mongo document of type `model` for the given request if
    it is permitted.
    If `args` (dict) is included then it will be used instead of
    the body of the request.
    `force_args` is a dict that will not be checked for permissions.
    '''
    try:
        args = args or request.get_json()
        permissions.check_create(model, args)
        args = {**args, **force_args}
        if model.__name__ == 'User':
            doc = _create_user(args)
        else:
            doc = model(**args)
            doc.save()

        metrics.track(
            event='{0}_created'.format(model.__name__.lower()),
            properties=doc.to_mongo().to_dict())

        return doc
    except ValidationError as e:
        raise InvalidData.from_validation_error(e, 'bad form data')
    except NotUniqueError as e:
        raise InvalidData.from_not_unique_error(e, 'bad form data')


def update(document, request):
    try:
        args = request.get_json()
        permissions.check_update(document, args)
        if document._class_name == 'User' and 'password' in args:
            args['password'] == hasher.hash_value(args['password'])
        elif document._class_name == 'PlaylistVideo' and 'sort_order' in args:
            PlaylistVideo.objects(
                    sort_order__gte=args['sort_order']).update(inc__sort_order=1)
            document.reload()
        document.modify(**args)

        # Metrics for document being edited
        update_document = document.to_mongo().to_dict()
        update_document['edited_by'] = current_user.id
        metrics.track(
            event='{0}_edited'.format(document._class_name.lower()),
            properties=update_document)

    except ValidationError as e:
        raise InvalidData.from_validation_error(e, 'bad form data')
    except NotUniqueError as e:
        raise InvalidData.from_not_unique_error(e, 'bad form data')


def delete(document, args={}):
    permissions.check_delete(document, args)

    # Metrics for document delete
    delete_document = document.to_mongo().to_dict()
    delete_document['deleted_by'] = current_user.id
    metrics.track(
        event='{0}_deleted'.format(document._class_name.lower()),
        properties=delete_document)

    document.delete()


def _create_user(args):
    if args.get('password', False):
        doc = User.register(**args)
    else:
        doc = User(**args)
        doc.save()

    try:
        vhx_user = vhx.create_user(email=doc.email)
        doc.modify(vhx_id=str(vhx_user['id']), vhx_source=vhx_user)
    except vhx.VHXError:
        doc.delete()
        raise ServiceUnavailable('There was an error creating the user')

    return doc
