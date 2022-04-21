"""
Mini api main file
"""
import json
from flask import Flask, Response


def create_app():
    """
    Factory function for flask application
    :return: app object
    """
    app = Flask(__name__)

    @app.get('/api/v1.0/first')
    def first_get():
        data = {
            'name': 'Jane',
            'age': 35
        }

        return Response(json.dumps(data), 200, content_type='application/json')

    @app.get('/api/v1.0/second')
    def second_get():
        data = {
            'name': 'Adam',
            'age': 36
        }

        return Response(json.dumps(data), 200, content_type='application/json')

    @app.get('/api/v1.0/third')
    def third_get():
        data = {
            'name': 'Anna',
            'age': 58
        }

        return Response(json.dumps(data), 200, content_type='application/json')

    return app


if __name__ == '__main__':
    create_app().run()
