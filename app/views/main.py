from flask import Blueprint, render_template

from ..models.post import Post


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    posts = Post.objects.all()
    return render_template('index.html', posts=posts)


@bp.route('/post/<id>')
def post(id):
    post = Post.objects.get(pk=id)
    return render_template('post.html', post=post)
