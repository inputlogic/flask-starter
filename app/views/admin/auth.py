from flask import redirect, render_template, request, url_for
from flask_login import current_user

from . import bp


@bp.before_request
def authenticate():
    ignored_endpoints = ('.login', '.logout')
    ignored_paths = [url_for(i) for i in ignored_endpoints]

    if request.path in ignored_paths:
        return None

    if current_user.is_authenticated:
        return None

    return redirect(url_for('.login'))


@bp.route('/login')
def login():
    return render_template('admin/login.html')


@bp.route('/logout')
def logout():
    pass
