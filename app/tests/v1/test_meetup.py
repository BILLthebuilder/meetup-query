# Third party imports
import unittest
import json

# Local imports
from app import create_app

class TestMeetups(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

    self.meetup_incomplete ={
            "topic" : "Programming"
        }
        self.meetup_complete ={
            "id": "1",
            "topic" : "Udacity welcom",
            "location" : "San Fransisco or remotely via zoom",
            "happeningOn" : "Tommorow"
        }

    # Test validity of json data in request
    def test_post_meetup(self):
        response = self.client.post('api/v1/meetups')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Only Application/JSON input expected")
        self.assertEqual(response.status_code, 400)
