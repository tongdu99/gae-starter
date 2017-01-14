import logging

from flask import Flask, render_template
from flask_restful import Api
from google.appengine.api import app_identity

from hello.HelloWorld import HelloWorld
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

app_id = app_identity.get_application_id()
host = "https://"+app_id

@app.route('/')
def home():
    url = host + '/api/1.0/helloworld'
    response = requests.get(url)
    return render_template('home.html', message=response.json()['message'])

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500