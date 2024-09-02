import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b"Welcome to Flask App!")

    def test_greet(self):
        response = self.app.get('/greet')
        self.assertIn(b"Hello, Guest! Welcome to your Flask app.", response.data)

    def test_time(self):
        response = self.app.get('/time')
        self.assertTrue(b"Current date and time:" in response.data)

    def test_hello_name(self):
        response = self.app.get('/hello/Wagner')
        self.assertEqual(response.data, b"Hello, Wagner!")

if __name__ == "__main__":
    unittest.main()
