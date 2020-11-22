import pytest
from pydometer import app
from os import remove

def test_uploads():
    response = app.test_client().get('/uploads')
    assert response.status_code==200

def test_uploads():
    response = app.test_client().get('/upload/test/data/female-167-70_walk1-100-10.txt')
    assert response.status_code==200

def test_create():
  response = app.test_client().post('/create', json={
      'data' : { 'tempfile': 'test/data/upload-1.txt'},
      'trial': { 'name': 'foo', 'rate': '100', 'steps': '10'},
      'user' : { 'gender': 'female', 'height': '157', 'stride': '90'}
  })

  assert response==302
  remove('public/uploads/female-157.0-90.0_foo-100-10.txt')
