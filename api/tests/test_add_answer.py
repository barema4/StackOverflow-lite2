"""
    Module for making tests on the app for sign in
"""
import unittest
import json
from run import app
class TestViews(unittest.TestCase):
    """"
        Class for making tests on sign in
        params: unittest.testCase
    """

    def setUp(self):
        """
           Method for making the client object
        """
        self.client = app.test_client
    def test_login(self):
        """
            Method for tesing the post function which logins in a user
        """
        result = self.client().post('/api/v1/questions/7/answers',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="ben", password="ben")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('msg', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 401)
        self.assertTrue(result.json["msg"])
    