from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.meetup_models import MeetupData


class Meetup(MeetupData, Resource):
    """ Endpoints for getting and posting all meetup records """

    def __init__(self):
        self.records = MeetupData()

    def post(self):
        """ The endpoint for creating a meetup entry """
        data = request.get_json()
        title = data['title']
        description = data['description']
        date = data['date']
        location = data['location']
        resp = self.records.save(title, description, date, location)
        return make_response(jsonify({
            "status": 201,
            "The Meetup is": resp}), 201)

    def get(self):
        """ The endpoint for getting all the meetup records """
        data = self.records.view_meetups()
        return make_response(jsonify({
            "status": 200,
            "All the meetups available are": data}), 200)


class Meetups(MeetupData, Resource):
    """Endpoints for getting specific meetups and updating meetup records"""

    def __init__(self):
        self.records = MeetupData()

    def get(self, id):
        """The endpoint for getting a specific meetup record"""
        data = self.records.view_one_meetup(id)
        if data is not None:
            return make_response(jsonify({
                "status": 200,
                "The specific meetup you are looking for is": data}), 200)
        else:

            return make_response(jsonify({
                "status": 404,
                "Message": "Sorry that Meetup was not found"}), 404)
            return make_response(jsonify({"Message": "Sorry that Meetup was not found"}), 404)
