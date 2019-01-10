from datetime import datetime, timedelta

QUESTIONS = []

class QuestionModel(object):
    """ Mapping question and data relations """

    def __init__(self):
        self.questions = QUESTIONS

    def create_question(self, title, body, meetup, createdby, votes):
        """ A constructor method for the questions """

        createdOn = datetime.now()
        meetup = {
            "id": len(self.questions) + 1,
            "title": title,
            "body": body,
            "meetup": meetup,
            "createdby": createdby,
            "createdon": createdOn,
            "votes": votes
        }

        self.questions.append(meetup)
        return meetup