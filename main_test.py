import unittest
import requests
import requests_toolbelt.adapters.appengine

from google.appengine.ext import testbed

requests_toolbelt.adapters.appengine.monkeypatch()

class MainTestCase(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_urlfetch_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def testHello(self):
        url = 'http://localhost:8080/'
        response = requests.get(url)
        self.assertEqual("Hello World!", response.content)