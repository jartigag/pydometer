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

@pytest.mark.parametrize("gender", ['invalid gender', 1])
def test_create_with_gender(gender):
    assert User().gender==None
    assert User(None).gender==None
    assert User('').gender==None

    with pytest.raises(ValueError) as e:
        User(gender)
    assert str(e.value)=="Invalid gender"

    assert User('Female').gender=='female'
    assert User('MALE').gender=='male'

@pytest.mark.parametrize("height", [0, '0', -1, '-1', 'invalid height'])
def test_create_with_height(height):
    assert User(None).height==None
    assert User(None, None).height==None
    assert User(None,'').height==None

    with pytest.raises(ValueError) as e:
        User(None, height=height)
    assert str(e.value)=="Invalid height"

@pytest.mark.parametrize("stride", [0, '0', -1, '-1', 'invalid stride'])
def test_create_with_stride(stride):
    assert User(None).stride==74
    assert User(None, None, None).stride==74
    assert User(None, None,'').stride==74

    with pytest.raises(ValueError) as e:
        User(None, None, stride=stride)
    assert str(e.value)=="Invalid stride"

    assert User(None, None, 80).stride==80
    assert User(None, None, '80').stride==80
    assert User(None, None, 80.0).stride==80
    assert User(None, None, '80.0').stride==80
    assert User(None, None, 75.25).stride==75.25
    assert User(None, None, '75.25').stride==75.25

def test_create_with_height_and_gender():
    assert User('male', 1).stride==0.415
    assert User('female', 1).stride==0.413

def test_calculate_stride():
    assert User().stride==74
    assert User('male').stride==78
    assert User('female').stride==70
    assert User(None, 200).stride==82.8
    assert User('male', 200).stride==83
    assert User('female', 200).stride==82.6
