import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


# ── Health ──────────────────────────────────────────────
def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json()['status'] == 'UP'
    assert res.get_json()['version'] == '1.0.0'


# ── Sum ─────────────────────────────────────────────────
def test_sum(client):
    res = client.post('/sum', json={'a': 5, 'b': 10})
    assert res.status_code == 200
    assert res.get_json()['result'] == 15

def test_sum_with_negative(client):
    res = client.post('/sum', json={'a': -5, 'b': 10})
    assert res.status_code == 200
    assert res.get_json()['result'] == 5

def test_sum_with_zero(client):
    res = client.post('/sum', json={'a': 0, 'b': 0})
    assert res.status_code == 200
    assert res.get_json()['result'] == 0

def test_sum_with_floats(client):
    res = client.post('/sum', json={'a': 1.5, 'b': 2.5})
    assert res.status_code == 200
    assert res.get_json()['result'] == 4.0

def test_sum_invalid_input(client):
    res = client.post('/sum', json={'a': 'hello', 'b': 10})
    assert res.status_code == 400
    assert 'error' in res.get_json()

def test_sum_missing_body(client):
    res = client.post('/sum', data='not json', content_type='text/plain')
    assert res.status_code == 400
    assert 'error' in res.get_json()


# ── Reverse String ───────────────────────────────────────
def test_reverse(client):
    res = client.post('/reverse-string', json={'text': 'hello'})
    assert res.status_code == 200
    assert res.get_json()['result'] == 'olleh'

def test_reverse_empty_string(client):
    res = client.post('/reverse-string', json={'text': ''})
    assert res.status_code == 200
    assert res.get_json()['result'] == ''

def test_reverse_single_char(client):
    res = client.post('/reverse-string', json={'text': 'a'})
    assert res.status_code == 200
    assert res.get_json()['result'] == 'a'

def test_reverse_invalid_input(client):
    res = client.post('/reverse-string', json={'text': 12345})
    assert res.status_code == 400
    assert 'error' in res.get_json()

def test_reverse_missing_body(client):
    res = client.post('/reverse-string', data='not json', content_type='text/plain')
    assert res.status_code == 400
    assert 'error' in res.get_json()


# ── Multiply ─────────────────────────────────────────────
def test_multiply(client):
    res = client.post('/multiply', json={'a': 3, 'b': 4})
    assert res.status_code == 200
    assert res.get_json()['result'] == 12

def test_multiply_by_zero(client):
    res = client.post('/multiply', json={'a': 5, 'b': 0})
    assert res.status_code == 200
    assert res.get_json()['result'] == 0

def test_multiply_negative(client):
    res = client.post('/multiply', json={'a': -3, 'b': 4})
    assert res.status_code == 200
    assert res.get_json()['result'] == -12

def test_multiply_floats(client):
    res = client.post('/multiply', json={'a': 2.5, 'b': 4.0})
    assert res.status_code == 200
    assert res.get_json()['result'] == 10.0

def test_multiply_invalid_input(client):
    res = client.post('/multiply', json={'a': 'x', 'b': 4})
    assert res.status_code == 400
    assert 'error' in res.get_json()


# ── Error Handlers ───────────────────────────────────────
def test_404_route(client):
    res = client.get('/nonexistent')
    assert res.status_code == 404
    assert res.get_json()['error'] == 'Route not found'

def test_405_wrong_method(client):
    res = client.get('/sum')
    assert res.status_code == 405
    assert res.get_json()['error'] == 'Method not allowed'