import unittest
import requests

from google.appengine.ext import testbed

class MainTestCase(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()

    def tearDown(self):
        self.testbed.deactivate()

    def testHello(self):
        url = 'http://localhost:8080/'
        response = requests.get(url)
        self.assertEqual("Hello World!", response.content)