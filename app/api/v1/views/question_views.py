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