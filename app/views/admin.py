from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_required

from ..forms.post import PostForm
from ..models.post import Post


bp = Blueprint('admin', __name__)


@bp.route('')
# @login_required
def posts():
    posts = Post.objects.all()
    return render_template('admin/index.html', posts=posts)


@bp.route('/new', methods=['GET', 'POST'])
# @login_required
def new_post():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(
            author=current_user.id,
            title=form.title.data,
            body=form.body.data)
        post.save()
        flash('Post created', 'success')
        return redirect(url_for('admin.posts'))

    return render_template(
        'admin/form.html',
        form=form,
        endpoint=url_for('.new_post'))


@bp.route('/edit/<id>', methods=['GET', 'POST'])
# @login_required
def edit_post(id):
    post = Post.objects.get(pk=id)
    form = PostForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        post.save()
        flash('Post updated', 'success')
        return redirect(url_for('admin.posts'))

    return render_template(
        'admin/form.html',
        form=form,
        endpoint=url_for('.edit_post', id=post.id))


@bp.route('/delete/<id>')
# @login_required
def delete_post(id):
    Post.objects(id=id).delete()
    flash('Post deleted', 'success')
    return redirect(url_for('admin.posts'))
