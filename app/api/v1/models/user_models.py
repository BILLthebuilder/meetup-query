from datetime import datetime, timedelta
import os, jwt

USERS = []

class UserModel(object):
    """ Create user class to map user data """
    
    def __init__(self):
        self.users = USERS
    
    def generate_auth_token(self, username):
        """ Method for auth token """
        try:
            payload = {'exp': datetime.utcnow() + timedelta(days=0, seconds=120), 'iat': datetime.utcnow(), 'sub': username}
            return jwt.encode(payload, os.getenv('SECRET_KEY', 'my_secret'), algorithm='HS256').decode('utf-8')
        except Exception as e:
            return e

    def verify_auth_token(self, auth_token):
        """Method to verify auth token """
        try:
            payload = jwt.decode(auth_token, os.getenv('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Token exppired, login again'
        except jwt.InvalidTokenError:
            return 'Invalid token, login'