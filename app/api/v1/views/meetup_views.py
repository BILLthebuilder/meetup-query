from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.meetup_models import MeetupData

class Meetup(MeetupData, Resource):
    """ Defining the class for the meetup """
    def __init__(self):
        self.records = MeetupData()

    def post(self):
        """ The endpoint for creating a meetup entry """
        data = request.get_json()
        title = data['Title']
        description = data['Description']
        date = data['Date']
        location = data['Location']
        resp = self.records.save(title, description, date, location)
        return make_response(jsonify({"The Meetup is": resp}), 201)

    def get(self):
        """ The endpoint for getting all the meetup records """
        data = self.records.view_meetups()
        return make_response(jsonify({"All the meetups available are": data}), 200)