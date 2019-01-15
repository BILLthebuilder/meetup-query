from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.vote_models import Votes


class Upvote(Votes, Resource):
    def __init__(self):
        self.vote_records = Votes()

    def patch(self, id):
        response = self.vote_records.vote(id, True)
        return make_response(jsonify({"My upvoted votes records are": response}), 201)
