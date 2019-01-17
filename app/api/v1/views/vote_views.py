from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.vote_models import Votes


class Upvote(Votes, Resource):
    def __init__(self):
        self.vote_records = Votes()

    def patch(self, id):
        response = self.vote_records.vote(id, True)
        return make_response(jsonify({
            "status": 201,
            "data": response
        }), 201)


class Downvote(Upvote, Votes, Resource):
    def __init__(self):
        super(Downvote, self).__init__()

    def patch(self, id):
        response = self.vote_records.vote(id, False)
        return make_response(jsonify({
            "status": 201,
            "data": response
        }), 201)
