"""
UNIT test for first end-point
"""

import json
from .fixture import client


def test_first_status_code(client):
    """
    Test the api HTTP status code
    :param client: A app test client from fixture
    :return: None
    """
    response = client.get('/api/v1.0/first')
    assert response.status_code == 200


def test_fist_data(client):
    """
    Test the data from a call to the first end-point
    :param client: A app test client from fixture
    :return: None
    """
    response = client.get('/api/v1.0/first')
    data = json.loads(response.text)
    assert data['name'] == 'Jane'
