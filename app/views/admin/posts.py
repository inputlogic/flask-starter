from flask import render_template

from app.forms.post import PostForm
from app.models.post import Post

from . import bp


@bp.route('')
def manage_posts():
    posts = Post.objects.all()
    return render_template('admin/index.html', posts=posts)


@bp.route('/new', methods=['GET', 'POST'])
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
def delete_post(id):
    Post.objects(id=id).delete()
    flash('Post deleted', 'success')
    return redirect(url_for('admin.posts'))
