from datetime import datetime, timedelta
import bcrypt

from app.models import db
import config


class ForgotPasswordToken(db.Document):
    user = db.ReferenceField('User')
    token = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.__hash_token()
        super(ForgotPasswordToken, self).save(*args, **kwargs)

    @staticmethod
    def validate_and_delete_token(id, token_string):
        '''Returns the user associated with token if valid'''
        token = ForgotPasswordToken.objects.get(id=id)
        token.delete()
        if token.__verify_token(token_string):
            return token.user
        raise ForgotPasswordToken.DoesNotExist

    def __repr__(self):
        return '<ForgotPasswordToken: {0}>'.format(self.id)

    def __verify_token(self, token):
        if self.__is_expired():
            return False
        return bcrypt.checkpw(
            token.encode('utf-8'),
            self.token.encode('utf-8'))

    def __hash_token(self):
        self.token = bcrypt.hashpw(
            self.token.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')

    def __is_expired(self):
        delta = timedelta(seconds=config.FORGOT_PASSWORD_TIMER)
        expiry = datetime.now() - delta
        return expiry > self.created_at
