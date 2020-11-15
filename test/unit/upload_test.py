#TODO: pytest or unittest?
from .models.parser import Parser
from .models.upload import Upload
#FIXME: ModuleNotFoundError: No module named '__main__.models'; '__main__' is not a package

def test_new_no_params():
    pass #TODO

def test_create():
    temp_file = 'test/data/upload-1.txt'
    file_path = 'public/uploads/female-999.0-90.0_run1-89-10.txt'
    user_params = { 'gender':'female', 'height':'999', 'stride':'90' }
    trial_params = { 'name':'run1', 'rate':'89', 'steps':'10' }
    #TODO

def test_find():
    file_path = 'public/uploads/female-168.0-70.0_walk1-100-100.txt'
    #TODO

def test_all():
    #TODO

def test_generate_file_path():
    file_path = 'public/uploads/female-999.0-90.0_bagwalk1-89-10.txt'
    user = User('female', '999', '90')
    trial = Trial('bagwalk1', '89', '10')
    #TODO:
    # assert Upload.generate_file_path(user, trial)==file_path
