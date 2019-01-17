from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.question_models import QuestionsModel


class Question(QuestionsModel, Resource):
    """ Posting the question """

    def __init__(self):
        self.questions_records = QuestionsModel()

    def post(self):
        """ The endpoint for posting a question """
        data = request.get_json()
        title = data['title']
        question = data['question']
        resp = self.questions_records.save(question, title)

        if resp is not None:
            return make_response(jsonify({
                "Status": 201,
                "The Questions are": resp}), 201)
        return make_response(jsonify({
            "Status": 500,
            "Error": "Question could not be posted"
        }), 500)
