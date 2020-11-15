#TODO: pytest or unittest?
from .models.user import User
#FIXME: ModuleNotFoundError: No module named '__main__.models'; '__main__' is not a package

def test_create():
    user = User.new('male', 167.5, 80)
    #TODO:
    # assert user.gender=='male'
    # assert user.height==167.5
    # assert user.stride==80

def test_create_no_params():
    user = User.new()
    #TODO:
    # assert user.gender==None
    # assert user.height==None
    # assert user.stride==74

def test_create_with_gender():
    #TODO

def test_create_with_height():
    #TODO

def test_create_with_stride():
    #TODO

def test_create_with_height_and_gender():
    #TODO

def test_calculate_stride():
    #TODO
