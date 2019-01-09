from flask import Flask, Blueprint, request, make_response, jsonify
from ..models import meetup_models
from werkzeug.exceptions import BadRequest

meetupv1 = Blueprint('meetups', __name__, url_prefix='/meetups')
meetups = meetup_models.MeetUpModel()


@meetupv1.route('', methods=['POST'])
def create_meetup():
    """ An endpoint to create meetups """

    try:
        data = request.get_json()
    except:
        return make_response(jsonify({
            "status": 400,
            "message": "Wrong input"
        })), 400
    topic = data.get('topic')
    location = data.get('location')
    images = data.get('images')
    happeningOn = data.get('happeningOn')
    tags = data.get('tags')

    if not topic:
        return make_response(jsonify({
            "status": 400,
            "message": "Provide a topic"
        })), 400
    if not location:
        return make_response(jsonify({
            "status": 400,
            "message": "Specify the location"
        })), 400
    if not happeningOn:
        return make_response(jsonify({
            "status": 400,
            "message": "Provide a date"
        })), 400
    if not tags:
        return make_response(jsonify({
            "status": 400,
            "message": "Provide a tag"
        })), 400
    else:
        meetup = meetups.create_meetup(
            topic, location, images, happeningOn, tags)
        return make_response(jsonify({
            "status": 201,
            "data": [{"topic": topic,
                      "location": location,
                      "happeningOn": happeningOn,
                      "tags": tags}]})), 201