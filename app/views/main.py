from flask import Blueprint, render_template

from ..models import post as post_model


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    posts = post_model.get_all()
    return render_template('index.html', posts=posts)


@bp.route('/post/<id>')
def post(id):
    post = post_model.get_by_id(id)
    return render_template('post.html', post=post)
