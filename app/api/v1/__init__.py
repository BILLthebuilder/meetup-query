from .views.rsvp_views import Reservations
from .views.question_views import Question
from .views.meetup_views import Meetup, Meetups
from .views.vote_views import Upvote
from flask_restful import Api
from flask import Blueprint

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api = Api(version_one)


# route that serves both POSTing and GETting meetup records
api.add_resource(Meetup, '/meetups')
# route to GET a specific meetup
api.add_resource(Meetups, '/meetups/<int:id>')
# route for POST question
api.add_resource(Question, '/questions')
# route to POST a reservation to a meetup
api.add_resource(Reservations, '/meetups/<int:id>/rsvp')
# route to upvote a question: PATCH
api.add_resource(Upvote, '/questions/<int:id>/upvote')
