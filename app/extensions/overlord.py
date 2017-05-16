from flask_overlord import admin

from ..models.user import User
from ..models.post import Post


def setup(app):
    admin.init_app(app)
    admin.add_model(User)
    admin.add_model(Post)

    @admin.route('/testing')
    def admin_reports():
        return 'custom route'

    # @admin.override('User', 'list')
    # def custom_user_list():
    #     return 'custom user list yay!'

    # @admin.override('User', 'edit')
    # def custom_user_edit(id='nope'):
    #     return 'The id is: {0}'.format(id)


# @admin.override('User', 'create')
# def custom_create(user):
#     pass
#
#
# @admin.route('/reports')
# def custom_reports():
#     return render_template('reports.html')
