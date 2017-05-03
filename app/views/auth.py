from flask import redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user

from .. import app, db, log
from ..forms import UserForm
from ..models.user import User


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()

    if form.validate_on_submit():
        try:
            user = User.register(email=form.email.data, password=form.password.data)
            login_user(user)
            return redirect(url_for('admin_posts'))
        except db.NotUniqueError:
            form._errors = True

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm()

    if form.validate_on_submit():
        try:
            user = User.validate_login(email=form.email.data, password=form.password.data)
            login_user(user)
            return redirect(url_for('admin_posts'))
        except User.DoesNotExist:
            form._errors = True

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
