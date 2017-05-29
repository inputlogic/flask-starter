from mongoengine.connection import get_db

import config
from app import create_app
from app.models import db


if config.ENV == config.PRODUCTION:
    response = input('Are you sure you want to drop the production db? [yes/no]')
    if response != 'yes':
        print('Phew, thats what I thought...')
        exit(0)
    print('If you say so...')


create_app()
get_db().client.drop_database(config.MONGODB_SETTINGS['db'])
