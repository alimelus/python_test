from app import hello_world, alive
from datetime import datetime

def test_hello_world():
    response = hello_world()
    assert 'Hello, world!' in response  # Adjust the assertion based on your expected template content

def test_alive():
    response = alive()
    assert response == "yes"

