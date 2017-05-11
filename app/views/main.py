from flask import abort, Blueprint, render_template

from .. import create_logger
from ..models import post as post_model
from ..models import user as user_model
from ..models.errors import NotFoundError


bp = Blueprint('main', __name__)
log = create_logger(__name__)


@bp.route('/')
def index():
    posts = post_model.get_all()
    return render_template('index.html', posts=list(posts))


@bp.route('/post/<id>')
def post(id):
    try:
        post = post_model.get_by_id(id)
        author = user_model.get_by_id(post['author'])
        return render_template('post.html', post=post, author=author)
    except NotFoundError:
        abort(404)
