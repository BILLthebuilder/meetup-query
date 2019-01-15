import datetime

QUESTIONS = []

class QuestionsModel():
    """ Mapping question and data relations """

    def __init__(self):
        self.questions = QUESTIONS

    def save(self, question):
        """ The questions db """

        q_data = {
            
            "createdOn": datetime.datetime.now(),
            "id" : len(self.questions) + 1,
            "question" : question
        }

        self.questions.append(q_data)
        return self.questions