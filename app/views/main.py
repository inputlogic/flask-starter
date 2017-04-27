from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user
from sqlalchemy.orm.exc import NoResultFound

from .. import app, db
from ..models.post import Post
from ..models.user import User


@app.route('/')
def index():
    return render_template('index.html', posts=Post.query.all())


@app.route('/post/<int:id>')
def post(id):
    q = Post.query.options(
        db.joinedload(Post.author),
        db.joinedload(Post.comments))
    q = q.get_or_404(id)
    return render_template('post.html', post=q)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        email = request.form.get('email')
        try:
            user = User.query.filter_by(email=email).one()
            login_user(user)
            return redirect(url_for('protected'))
        except NoResultFound:
            error = 'Invalid login details'

    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/protected')
@login_required
def protected():
    return render_template('protected.html')
