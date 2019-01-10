from datetime import datetime, timedelta
import os, jwt

USERS = []

class UserModel(object):
    """ Create user class to map user data """
    
    def __init__(self):
        self.users = USERS
    
    