from app import index

def test_index():
    result = index()
    expected = "Hello, world!"
    assert result == expected
