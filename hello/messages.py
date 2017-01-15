from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello World'}


class HelloMessage(Resource):
    def get(self):
        return {'messages': ['Hello City', 'Hello Country', 'Hello World', 'Hello Universe']}
