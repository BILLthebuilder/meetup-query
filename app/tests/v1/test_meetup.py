# # Third party imports
# import unittest
# import json

# # Local imports
# from app import create_app

# class TestMeetups(unittest.TestCase):

#     def setUp(self):
#         self.app = create_app("testing")
#         self.client = self.app.test_client()

#         self.meetup_incomplete ={
#                 "topic" : "Programming"
#             }
#         self.meetup_complete ={
#             "id": "1",
#             "topic" : "Udacity welcom",
#             "location" : "San Fransisco or remotely via zoom",
#             "happeningOn" : "Tommorow"
#         }

#     # Test validity of json data in request
#     def test_post_meetup(self):
#         response = self.client.post('api/v1/meetups')
#         result = json.loads(response.data)
#         self.assertEqual(result["message"],"Only Application/JSON input expected")
#         self.assertEqual(response.status_code, 400)

#      # Test empty fields
#     def test_post_empty_meetup(self):
#         response = self.client.post('api/v1/meetups',data=json.dumps(self.meetup_incomplete),
#         content_type="application/json")
#         result = json.loads(response.data)
#         self.assertEqual(result["message"],"All fields must be populated with data")
#         self.assertEqual(response.status_code, 400)

#     # Test valid input for meetup creation
#     def test_post_meetup_success(self):
#         response = self.client.post('api/v1/meetups', data=json.dumps(self.meetup_complete),
#         content_type="application/json")
#         result = json.loads(response.data)
#         self.assertEqual(result["message"],"Meetup created succesfully")
#         self.assertEqual(response.status_code, 201)


import unittest
import json

from app import create_app


class TestMeetups(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

    def create_record(self):
        response = self.client.post('/api/v1/meetups',
                                    data=json.dumps({
                                        "title": "Football",
                                        "description": "Playing football on 25th",
                                        "date": "25th of November",
                                        "location": "Kasarani"
                                    }),
                                    headers={"content-type": "application/json"})
        return response

    # Test meetups creation
    def test_01_post_meetups(self):
        response = self.create_record()
        self.assertEqual(response.status_code, 201)

    # Test for fetching all meetup records
    def test_02_get_all(self):
        response = self.client.get('/api/v1/meetups',
                                   headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 200)

    # Test for getting a specific meetup record
    def test_03_get_specific(self):
        self.create_record()
        response = self.client.get('/api/v1/meetups/1',
                                   headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
