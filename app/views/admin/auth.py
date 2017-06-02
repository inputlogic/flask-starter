from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

from app.forms.user import AuthForm
from app.models.user import User

from . import bp


@bp.before_request
def authenticate():
    ignored_endpoints = ('.login', '.logout')
    ignored_paths = [url_for(i) for i in ignored_endpoints]

    if request.path in ignored_paths:
        return None

    if current_user.is_authenticated and current_user.is_admin:
        return None

    return redirect(url_for('.login'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = AuthForm()

    if form.validate_on_submit():
        try:
            user = User.validate_login(
                email=form.email.data,
                password=form.password.data)
            if user.is_admin:
                login_user(user)
                return redirect(url_for('admin.manage_users'))
        except User.DoesNotExist:
            pass
        form._errors = True

    if form.errors:
        flash('Invalid login details', 'warning')

    return render_template('admin/login.html', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    flash('You\'ve been logged out', 'success')
    return redirect(url_for('.login'))
