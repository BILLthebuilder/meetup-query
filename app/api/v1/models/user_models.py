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