from flask import render_template
from flask_login import login_required

from .. import app


@app.route('/admin')
@login_required
def admin_posts():
    return render_template('admin/index.html')


@app.route('/admin/new')
@login_required
def admin_new_post():
    return render_template('admin/new.html')


@app.route('/admin/edit/<int:id>')
@login_required
def admin_edit_post(id):
    return render_template('admin/edit.html')


@app.route('/admin/delete/<int:id>')
@login_required
def admin_delete_post(id):
    return render_template('admin/delete.html')
