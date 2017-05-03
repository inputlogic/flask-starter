from flask import render_template

from .. import app
from ..models.post import Post


@app.route('/')
def index():
    posts = Post.objects.all()
    return render_template('index.html', posts=posts)


@app.route('/post/<id>')
def post(id):
    post = Post.objects.get(pk=id)
    return render_template('post.html', post=post)
