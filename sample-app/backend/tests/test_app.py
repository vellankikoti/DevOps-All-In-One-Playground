import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the DevOps-All-In-One Quiz API!", response.data)

    def test_start_quiz(self):
        response = self.app.post('/start/test_user')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hi test_user, let's begin the quiz", response.data)

if __name__ == '__main__':
    unittest.main()
