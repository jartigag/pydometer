import pytest

from pydometer.models.user import User

def test_create():
    user = User('male', 167.5, 80)

    assert user.gender=='male'
    assert user.height==167.5
    assert user.stride==80

def test_create_no_params():
    user = User()

    assert user.gender==None
    assert user.height==None
    assert user.stride==74

def test_create_with_gender():
    pass #TODO

def test_create_with_height():
    pass #TODO

def test_create_with_stride():
    pass #TODO

def test_create_with_height_and_gender():
    pass #TODO

def test_calculate_stride():
    pass #TODO
