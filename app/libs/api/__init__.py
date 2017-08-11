'''
Format mongo resource(s) or AppError (see error lib) to appropriate API format.
'''

from flask_mongoengine import BaseQuerySet
from flask import url_for
import math

from app.libs.errors import UnprocessableEntity
import config


def format(data, request, serializer, url=None, includes={}):
    '''
    Format a resource or resources based on rest api specs.
    Includes the following formatting:
    - serializes resource(s) and limits fields based on request `fields` query param
    - paginates response if data is a list (gets page and page size from query params)
    - includes resources specified in 'include' query param and supported by
      'includes' argument
    - returns data and includes (if provided) following the api specification

    Includes should map any accepted "include" query param value to a function.
    The function should expect the main resource (data param) and return
    the resources to be included.

    '''
    fields = request.args.get('fields')

    if data.__class__.__name__ == 'BaseQuerySet':
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 0))
        data, pagination = _paginate(data, url, request.args, page, page_size)
        return {'data': _serialize(data, serializer, fields), **pagination}
    else:
        requested_includes = request.args.getlist('include')
        included = _includes(data, requested_includes, includes)
        included = {k: _serialize(v, serializer) for k, v in included.items()}
        included = {'included': included} if len(included.keys()) > 0 else {}
        return {'data': _serialize(data, serializer, fields), **included}


def error(e):
    '''
    Expects an AppError exception.
    Returns the error following api specification.

    '''
    response = {
            'code': e.status_code,
            'message': e.message,
            'type': e.name
            }

    if hasattr(e, 'fields'):
        response['fields'] = e.fields

    return response


def _includes(resource, requested_includes, includes):
    '''
    Return a dict of included resources
    includes should be a dict that maps an include name (that will come from
    url query) to a function that expects the main resource and returns the
    included resources for that name:
    { '<include-name>': resource -> resource(s) }

    '''
    requested = set(requested_includes)
    valid = set(includes.keys())
    if not requested <= valid:
        invalid = requested - valid
        raise UnprocessableEntity(
                'The following includes are not supported: {}'.format(
                    ', '.join(invalid)))

    return {k: v(resource) for k, v in includes.items()}


def _serialize(data, serializer, fields=None):
    if isinstance(data, BaseQuerySet):
        return [serializer(doc, fields) for doc in data]
    else:
        return serializer(data, fields)


def _paginate(
    resources,
    url,
    query_params,
    page=1,
    page_size=getattr(config, 'DEFAULT_PAGE_SIZE', 20)
):
    count = len(resources)
    page_size = config.DEFAULT_PAGE_SIZE if page_size < 1 else page_size
    pages = count / page_size
    pages = math.ceil(pages) if pages > math.floor(pages) else pages
    next_page = page + 1 if page + 1 <= pages and page > 0 else None
    prev_page = page - 1 if page > 1 and page <= pages else None

    next_params = {**query_params, 'page': next_page}
    prev_params = {**query_params, 'page': prev_page}

    if callable(url):
        next_url = next_page and url(**next_params) or None
        prev_url = prev_page and url(**prev_params) or None
    else:
        next_url = next_page and url_for(url, **next_params) or None
        prev_url = prev_page and url_for(url, **prev_params) or None

    resources = resources.skip(page_size * (page - 1)).limit(page_size)

    return resources, {
            'page': page,
            'page_size': page_size,
            'pages': pages,
            'next_page': next_url,
            'prev_page': prev_url,
            'count': count}
