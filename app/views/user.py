from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user

from ..forms import UserForm
from ..models import user as user_model


bp = Blueprint('user', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()

    if form.validate_on_submit():
        user = user_model.register(
            email=form.email.data,
            password=form.password.data)

        if user:
            login_user(user)
            return redirect(url_for('admin.posts'))

        form._errors = True

    return render_template('register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm()

    if form.validate_on_submit():
        user = user_model.validate_login(
            email=form.email.data,
            password=form.password.data)

        if user:
            login_user(user)
            return redirect(url_for('admin.posts'))

        form._errors = True

    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))
