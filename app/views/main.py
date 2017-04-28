from flask import render_template

from .. import app, db
from ..models.post import Post


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
