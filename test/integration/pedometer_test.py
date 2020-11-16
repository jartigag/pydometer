import pytest

def test_uploads():
    pass
    #TODO: assert_equal 200, last_response.status

def test_uploads():
  pass
  #TODO:
  # get '/upload/test/data/female-167-70_bagwalk1-100-10.txt'
  # assert_equal 200, last_response.status

def test_create():
  pass
  #TODO:
  # post '/create', {
  #   'data'  => { 'tempfile' => 'test/data/upload-1.txt' },
  #   'trial' => { 'name' => 'foo', 'rate' => '100', 'steps' => '10' },
  #   'user'  => { 'gender' => 'female', 'height' => '157', 'stride' => '90' }
  # }

  # assert_equal 302, last_response.status
  # rm('public/uploads/female-157.0-90.0_foo-100-10.txt')
