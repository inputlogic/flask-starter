from flask import render_template

from app.models.post import Post
from . import bp


@bp.route('/')
def index():
    posts = Post.objects.all()
    return render_template('index.html', posts=posts)


@bp.route('/post/<id>')
def post(id):
    post = Post.objects.get(pk=id)
    return render_template('post.html', post=post)
