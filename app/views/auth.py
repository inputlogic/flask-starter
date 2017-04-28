from flask import redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user
from sqlalchemy.orm.exc import NoResultFound

from .. import app
from ..forms import LoginForm
from ..models.user import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).one()
            login_user(user)
            return redirect('admin_posts')
        except NoResultFound:
            # Manually set form.errors to show generic error in form
            form._errors = True

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
