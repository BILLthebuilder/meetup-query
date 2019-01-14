from flask_restful import Api
from flask import Blueprint

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api = Api(version_one)

from .views.meetup_views import Meetup, Meetups

api.add_resource(Meetup, '/meetups') #route for POST and GET for meetup records
api.add_resource(Meetups,'/meetups/<int:id>') # route to GET a specific meetup

