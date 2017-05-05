from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_required

from ..forms import PostForm
from ..models.post import Post


bp = Blueprint('admin', __name__)


@bp.route('/admin')
@login_required
def posts():
    posts = Post.objects.all()
    return render_template('admin/index.html', posts=posts)


@bp.route('/admin/new')
@login_required
def new_post():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(
            author=current_user,
            title=form.title.data,
            body=form.body.data)
        post.save()
        flash('Post created')
        return redirect(url_for('admin.posts'))

    return render_template('admin/new.html', form=form)


@bp.route('/admin/edit/<id>')
@login_required
def edit_post(id):
    return render_template('admin/edit.html')


@bp.route('/admin/delete/<id>')
@login_required
def delete_post(id):
    return render_template('admin/delete.html')
