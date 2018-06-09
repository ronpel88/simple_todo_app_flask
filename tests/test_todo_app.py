import os
import sys
import unittest
import requests
from flask_api import FlaskAPI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/todo_app")
# app = FlaskAPI(__name__)

class BasicAppTests(unittest.TestCase):
    """ Unittests """

    def test_example(self):
        self.assertEqual(True, True)

if __name__ == "__main__":
    unittest.main()