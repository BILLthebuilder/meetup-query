from flask import Flask, Blueprint, request, make_response, jsonify
from ..models import question_models
from werkzeug.exceptions import BadRequest

questionsv1 = Blueprint('questions', __name__, url_prefix='/api/v1/questions')
questions = question_models.QuestionModel()


@questionsv1.route('', methods=['POST'])
def create_question():
    """ An Endpoint for creating a question about a meetup """

    try:
        data = request.get_json()
    except:
        return make_response(jsonify({
            "status": 400,
            "message": "Wrong input"
        })), 400

    title = data.get('title')
    body = data.get('body')
    meetup = data.get('meetup')
    createdby = data.get('createdby')
    votes = data.get('votes')

    if not title:
        return make_response(jsonify({
            "status": 400,
            "message": "Please provide a topic"
        })), 400

    if not body:
        return make_response(jsonify({
            "status": 400,
            "message": "Specify the location"
        })), 400

    if not meetup:
        return make_response(jsonify({
            "status": 400,
            "message": "Please provide the meetup that you are asking for"
        })), 400

    if not createdby:
        return make_response(jsonify({
            "status": 400,
            "message": "Please specify the creator"
        })), 400
    question = questions.create_question(
            title, body, meetup, createdby, votes)
    return make_response(jsonify({
        "status": 201,
        "data": [{
            "title": title,
            "body": body,
            "meetup": meetup,
            "user": createdby,
        }]})), 201
