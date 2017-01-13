import logging

from flask import Flask, render_template
from flask_restful import Api
from hello.HelloWorld import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/api/1.0/helloworld')


@app.route('/')
def home():
    return render_template('home.html')

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500