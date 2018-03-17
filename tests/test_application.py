# -*- coding: utf-8 -*-
''' Boby Mass Index Challenge Tests

    Tests the BMI application
'''

import os
import sys
import unittest
import tempfile

# Properly setup the PYTHONPATH
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../')

from application import create_app


class ApplicationTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(tempfile.mkstemp())

    def tearDown(self):
        pass

    def login(self, email, password):
        return self.app.post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_dummy(self):
        pass


if __name__ == '__main__':
    unittest.main()
