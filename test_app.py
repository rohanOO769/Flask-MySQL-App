import unittest
import json
from flask import Flask
from flask.testing import FlaskClient

from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get_test_word(self):
        response = self.app.get('/api/test')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertIn('word', data)
        self.assertIsInstance(data['word'], str)

    def test_get_test_word_no_word_found(self):
        # Assuming the database is empty
        # Run your setup to clear the database or ensure no word is present

        response = self.app.get('/api/test')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertIn('word', data)
        self.assertEqual(data['word'], 'No word found')

if __name__ == '__main__':
    unittest.main()
