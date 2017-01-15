from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello World'}


class HelloMessage(Resource):
    def get(self):
        return {'messages': ['Hello City', 'Hello Country', 'Hello World', 'Hello Universe']}


class HelloMessageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(120), unique=True)