import unittest
import json

from app import create_app


class TestRsvp(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

    def create_rsvp(self):
        response = self.client.post('/api/v1/meetups/1/rsvp',
                                    data=json.dumps({
                                        "topic": "Learning Javascript",
                                        "status": "going"
                                    }),
                                    headers={"content-type": "application/json"})
        return response

    # Test for rsvp of a meetup
    def test_rsvp_meetup(self):
        response = self.create_rsvp()
        self.assertEqual(response.status_code, 201)
