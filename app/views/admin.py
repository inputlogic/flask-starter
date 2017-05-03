from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_required

from .. import app
from ..forms import PostForm
from ..models.post import Post


@app.route('/admin')
@login_required
def admin_posts():
    posts = Post.objects.all()
    return render_template('admin/index.html', posts=posts)


@app.route('/admin/new')
@login_required
def admin_new_post():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(
            author=current_user,
            title=form.title.data,
            body=form.body.data)
        post.save()
        flash('Post created')
        return redirect(url_for('admin_posts'))

    return render_template('admin/new.html', form=form)


@app.route('/admin/edit/<id>')
@login_required
def admin_edit_post(id):
    return render_template('admin/edit.html')


@app.route('/admin/delete/<id>')
@login_required
def admin_delete_post(id):
    return render_template('admin/delete.html')
