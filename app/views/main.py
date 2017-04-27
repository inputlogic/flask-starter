from flask import render_template

from .. import app, db
from ..models.post import Post


@app.route('/')
def index():
    posts = db.session.query(Post).all()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:id>')
def post(id):
    q = db.session.query(Post)
    # Join related author and comments to avoid additional queries
    q = q.options(
        db.joinedload(Post.author),
        db.joinedload(Post.comments))
    q = q.get(id)
    return render_template('post.html', post=q)
