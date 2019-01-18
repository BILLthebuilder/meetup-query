import datetime

VOTES = []


class Votes():

    """Map vote models and data relations"""

    def __init__(self):
        self.vote_records = VOTES

    def find_vote(self, id):
        response = None
        for item in self.vote_records:
            if item['meetup_id'] == id:
                response = item
        return response

    def save(self, id, vote):

        data = {
            "meetup_id": id,
            "votes": 0,
            "voted_on": datetime.datetime.now()
        }

        if vote:
            data['votes'] += 1

        elif data['votes'] > 0:
            data['downvotes'] -= 1
        self.vote_records.append(data)
        return self.vote_records

    def vote(self, id, vote):
        record = self.find_vote(id)
        if record is not None:  # Record exists...
            if vote:
                record['votes'] += 1
            elif record['votes'] > 0:
                record['votes'] -= 1
            return record
        else:  # record does not exists
            response = self.save(id, vote)
        return response
