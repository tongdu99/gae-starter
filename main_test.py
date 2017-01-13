import unittest
import requests
from selenium import webdriver

from google.appengine.ext import testbed


class MainTestCase(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()

    def tearDown(self):
        self.testbed.deactivate()

    def testHello(self):
        url = 'http://localhost:8080/api/1.0/helloworld'
        response = requests.get(url)
        self.assertEqual('{"Hello": "World"}\n', response.content)

    def testHome(self):
        url = 'http://localhost:8080'
        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get(url)
        helloworld = driver.find_element_by_tag_name("p")
        self.assertEqual('Hello World', helloworld.text)
