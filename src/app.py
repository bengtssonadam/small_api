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

    @app.get('/ap1/v1.0/first')
    def first_get():
        data = {
            'name': 'Jane',
            'age': 35
        }

        return Response(json.dumps(data), 200, content_type='application/json')

    return app


if __name__ == '__main__':
    create_app().run()
