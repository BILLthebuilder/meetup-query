import datetime

VOTES = []


class Votes():

    """Map vote models and data relations"""

    def __init__(self):
        self.vote_records = VOTES

    def find_vote(self, id):
        response = None
        for each_item in self.vote_records:
            if each_item['question_id'] == id:
                response = each_item
        return response

    def vote(self, id, vote):
        record = self.find_vote(id)
        if record is not None:
            record['upvotes'] += 1
            return record
        else:
            response = self.save(id, vote)
        return response

    def save(self, id, vote):

        data = {
            "question_id": id,
            "upvotes": 0,
            "downvotes": 0,
            "voted_on": datetime.datetime.now()
        }
        # Checking for upvotes
        if vote:
            data['upvotes'] += 1

        # Checking for downvotes
        else:
            data['downvotes'] += 1
        self.vote_records.append(data)
        return self.vote_records
