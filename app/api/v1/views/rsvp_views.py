from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.rsvp_models import RsvpModel


class Reservations(RsvpModel, Resource):
    """ Posting the reservation """

    def __init__(self):
        self.reserve_records = RsvpModel()

    def post(self, id):
        """ The endpoint to rsvp to a meetup"""
        data = request.get_json()
        topic = data['topic']
        status = data['status']
        resp = self.reserve_records.save(id, topic, status)

        if resp is not None:
            return make_response(jsonify({
                "status": 201,
                "data": resp
            }), 201)
        return make_response(jsonify({
            "status": 500,
            "error": "unable to book reservation"
        }), 500)
