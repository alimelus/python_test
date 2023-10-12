from app import app
from datetime import datetime

def test_hello_world():
    client = app.test_client()
    response = client.get('/')
    assert b'Hello, world!' in response.data

def test_alive():
    client = app.test_client()
    response = client.get('/alive')
    assert response.data == b'yes'
