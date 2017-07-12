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
    form = UserForm()
    form_url = url_for('.create_user')

    if form.validate_on_submit():
        user = User()
        user = User.register(
                email=form.email.data,
                password=form.password.data,
                is_admin=form.is_admin.data)
        user.save()
        flash('User created', 'success')
        return redirect(url_for('.manage_users'))

    return render_template(
        'admin/users/form.html',
        form=form,
        form_url=form_url)


@bp.route('/users/<id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.objects.get_or_404(pk=id)
    form = UserForm(obj=user)
    form_url = url_for('.edit_user', id=id)

    if form.validate_on_submit():
        form.populate_obj(user)
        user.save()
        flash('User updated', 'success')

    return render_template(
        'admin/users/form.html',
        user=user,
        form=form,
        form_url=form_url)


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
