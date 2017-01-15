import logging
import os

from flask import Flask, render_template
from flask_restful import Api
from google.appengine.api import app_identity

from hello.messages import HelloWorld, HelloMessage

import requests
from requests_toolbelt.adapters import appengine

s = requests.Session()
s.mount('http://', appengine.AppEngineAdapter())
s.mount('https://', appengine.AppEngineAdapter())
# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
appengine.monkeypatch()

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/api/1.0/helloworld')
api.add_resource(HelloMessage, '/api/1.0/hellomessage')

url_prefix = "http://"
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
    url_prefix = "https://"

host_name = app_identity.get_default_version_hostname()
url_base = url_prefix+host_name


@app.route('/')
def home():
    url = url_base + '/api/1.0/helloworld'
    # message = requests.get(url).json()['message']
    # return render_template('home.html', message=message)
    response = requests.get(url)
    return render_template('home.html', message=response.json()['message'])

@app.route('/messages')
def message_list():
    url = url_base + '/api/1.0/hellomessage'
    messages = requests.get(url).json()['messages']
    return render_template('messages.html', messages=messages)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
