import unittest

from flask import Flask

from app import app


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        response = self.app.get('/home')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ayurveda Hospital', response.data)

    def test_payment_page(self):
        response = self.app.get('/pay')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Payment', response.data)

    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_logout_page(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ayurveda Hospital', response.data)

    def test_new_patient_page(self):
        response = self.app.get('/new')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register Now', response.data)

if __name__ == '__main__':
    unittest.main()
