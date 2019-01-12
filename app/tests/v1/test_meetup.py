# Third party imports
import unittest
import json

# Local imports
from app import create_app

class TestMeetups(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

    def create_record(self):
        response = self.client.post('/api/v1/meetups', \
            data=json.dumps({
                "Title": "Udacity",
                "Description": "A meetup for udacity Alumni will be this Tuesday",
                "Date" : "Tuesday Next week",
                "Location" : "San Fransisco or remote via zoom"
                }),\
            headers={"content-type": "application/json"})
        return response

    #Test the creation of a meetup
    def test_01_post(self):
        response = self.create_record()
        self.assertEqual(response.status_code, 201)