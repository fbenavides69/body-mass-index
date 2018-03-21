# -*- coding: utf-8 -*-
''' Boby Mass Index Challenge Tests

    Tests the BMI application
'''

import os
import sys
import unittest
import pytest


# Properly setup the PYTHONPATH
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../')

from application import create_app


TEST_DB = 'sqlite:////tmp/test.db'


class ApplicationTest(unittest.TestCase):

    email = 'test@testing.com'
    password = 'password'
    confirm = 'password'

    # Executed before each test case
    def setUp(self):
        app, self.db = create_app(TEST_DB)
        self.app = app.test_client()
        self.app.testing = True
        self.db.create_all()

    # Executed after each test case
    def tearDown(self):
        pass

    def index(self):
        return self.app.get('/', follow_redirects=True)

    def register_get(self):
        return self.app.get('/register', follow_redirects=True)

    def register_post(self, email, password, confirm):
        return self.app.post(
            '/register',
            data=dict(email=email, password=password, confirm=confirm),
            follow_redirects=True
        )

    def login_get(self):
        return self.app.get('/login', follow_redirects=True)

    def login_post(self, email, password):
        return self.app.post(
            '/login',
            data=dict(email=email, password=password),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    # Successful test cases

    def test_index(self):
        response = self.index()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_registration(self):
        response = self.register_get()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)

    def test_login(self):
        response = self.login_get()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_registered(self):
        response = self.register_post(self.email, self.password, self.confirm)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'BMI Calculator', response.data)

    def test_registered_logout(self):
        response = self.logout()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_loggedin(self):
        response = self.login_post(self.email, self.password)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'BMI Calculator', response.data)

    def test_loggedin_logout(self):
        response = self.logout()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)


if __name__ == '__main__':
    unittest.main()
