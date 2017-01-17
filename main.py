import logging
import os

from flask import Flask, render_template
from flask_restful import Api
from google.appengine.api import app_identity

from hello.messages import HelloWorld, HelloMessage, db

import requests
from requests_toolbelt.adapters import appengine
from urllib import quote_plus as urlquote

s = requests.Session()
s.mount('http://', appengine.AppEngineAdapter())
s.mount('https://', appengine.AppEngineAdapter())
# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
appengine.monkeypatch()

app = Flask(__name__)


# local setting
url_prefix = "http://"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dev:mysql@localhost/gae-starter'
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
    # app engine setting
    url_prefix = "https://"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:legaldocker@/gae-starter?unix_socket=/cloudsql/legaldocker:us-central1:legaldocker'

api = Api(app)
db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
db.init_app(app)
with app.app_context():
    db.create_all()

api.add_resource(HelloWorld, '/api/1.0/helloworld')
api.add_resource(HelloMessage, '/api/1.0/hellomessage')

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
    messages = requests.get(url).json()
    return render_template('messages.html', messages=messages)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
