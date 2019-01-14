import unittest
import json

from app import create_app

class TestQuestions(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

    def create_record(self):
        response = self.client.post('/api/v1/questions', 
            data=json.dumps({
                "Title": "Javascript",
                "question" : "How do you write Promises?"
                }),
            headers={"content-type": "application/json"})
        return response

    #Test questions creation
    def test_01_post_questions(self):
        response = self.create_record()
        self.assertEqual(response.status_code, 201)