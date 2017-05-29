from flask import flash, redirect, render_template, url_for
from flask_login import current_user

from . import bp
from app.models.user import User


@bp.route('/users')
def manage_users():
    users = User.objects.all()
    return render_template('admin/users/index.html', users=users)


@bp.route('/users/create')
def create_user():
    return render_template('admin/users/create.html')


@bp.route('/users/<id>')
def edit_user(id):
    user = User.objects.get_or_404(pk=id)
    return render_template('admin/users/edit.html', user=user)


@bp.route('/users/<id>/delete')
def delete_user(id):
    if current_user.id == id:
        flash('You can delete yourself', 'warning')
    else:
        user = User.objects.get_or_404(pk=id)
        user.delete()
        flash('User deleted', 'success')
        
    return redirect(url_for('.manage_useres'))
