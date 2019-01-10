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
            return 'Token expired, please login again'
        except jwt.InvalidTokenError:
            return 'Invalid token, please login'

    def signup(self, firstname, lastname, othername, email, phoneNumber, username, isAdmin, password):
        """ Method to add new users """

        registered = datetime.now()
        user = {
            "id": len(self.users) + 1,
            "firstname": firstname,
            "lastname": lastname,
            "othername": othername,
            "email": email,
            "phoneNumber": phoneNumber,
            "username": username,
            "registered": registered,
            "isAdmin": isAdmin,
            "password": password
        }