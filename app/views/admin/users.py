from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user

from . import bp
from app import create_logger
from app.forms.user import UserForm
from app.models.user import User


log = create_logger(__name__)


@bp.route('/users')
def manage_users():
    users = User.objects.all()
    return render_template('admin/users/index.html', users=users)


@bp.route('/users/create', methods=['GET', 'POST'])
def create_user():
    return render_template('admin/users/create.html')


@bp.route('/users/<id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.objects.get_or_404(pk=id)
    form = UserForm(obj=user)

    if form.validate_on_submit():
        log.debug('saving user')
        form.populate_obj(user)
        user.save()
        flash('User updated', 'success')
    else:
        log.debug(form.errors)

    return render_template('admin/users/edit.html', user=user, form=form)


@bp.route('/users/<id>/delete', methods=['GET', 'POST'])
def delete_user(id):
    user = User.objects.get_or_404(pk=id)

    if str(current_user.id) == str(id):
        flash('You can delete yourself', 'warning')
        return redirect(url_for('.manage_users'))

    elif request.method == 'POST':
        user = User.objects.get_or_404(pk=id)
        user.delete()
        flash('User deleted', 'success')
        return redirect(url_for('.manage_users'))

    return render_template('admin/users/delete.html', user=user)
