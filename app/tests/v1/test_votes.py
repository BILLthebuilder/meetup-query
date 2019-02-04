import unittest
import json


from app import create_app


class TestRsvp(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

    def up_vote(self):
        response = self.client.patch('api/v1/questions/1/upvote',
                                     data=json.dumps({
                                         "meetup_id": 1,
                                         "votes": 1
                                     }),
                                     headers={"content-type": "application/json"})
        return response

    # Test for upvoting of a question
    def test_upvote(self):
        response = self.up_vote()
        self.assertEqual(response.status_code, 201)

    def down_vote(self):
        response = self.client.patch('api/v1/questions/1/downvote',
                                     data=json.dumps({
                                         "meetup_id": 1,
                                         "votes": 1
                                     }),
                                     headers={"content-type": "application/json"})
        return response

    # Test for downvoting of a question
    def test_downvote(self):
        response = self.down_vote()
        self.assertEqual(response.status_code, 201)
