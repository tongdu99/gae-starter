import unittest
import requests
from selenium import webdriver

from google.appengine.ext import testbed


class MainTestCase(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.url_base = 'http://127.0.0.1:8080'
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')

    def tearDown(self):
        self.testbed.deactivate()

    def testHello(self):
        url = 'http://127.0.0.1:8080/api/1.0/helloworld'
        response = requests.get(url)
        self.assertEqual("Hello World", response.json()['message'])

    def testHome(self):
        self.driver.get(self.url_base)
        helloworld = self.driver.find_element_by_tag_name("p")
        self.assertEqual('Hello World', helloworld.text)

    def testMessages(self):
        self.driver.get(self.url_base+"/messages")
        message_elements = self.driver.find_elements_by_tag_name("h2")
        messages = [msg.text for msg in message_elements]
        self.assertSequenceEqual(messages, ['Hello City', 'Hello Country', 'Hello World', 'Hello Universe'])

