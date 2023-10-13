from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_alive(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data == b"yes"


