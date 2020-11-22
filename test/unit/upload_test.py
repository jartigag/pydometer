import pytest
from os import remove

from models.parser import Parser
from models.upload import Upload
from models.user import User
from models.trial import Trial

def test_new_no_params():
    with pytest.raises(ValueError) as e:
        Upload()
    assert str(e.value)=="A file path or user and trial parameters must be provided."

def test_create():
    temp_file = 'test/data/upload-1.txt'
    file_path = 'public/uploads/female-999-90_run1-89-10.txt'
    user_params = { 'gender':'female', 'height':'999', 'stride':'90' }
    trial_params = { 'name':'run1', 'rate':'89', 'steps':'10' }

    upload = Upload.create(temp_file, user_params, trial_params)

    assert upload.user.gender==user_params['gender']
    assert upload.user.height==float(user_params['height'])
    assert upload.user.stride==float(user_params['stride'])

    assert upload.trial.name==trial_params['name']
    assert upload.trial.rate==int(trial_params['rate'])
    assert upload.trial.steps==int(trial_params['steps'])

    remove(file_path)

def test_find():
    file_path = 'public/uploads/female-168-70_walk1-100-100.txt'
    upload = Upload.find(file_path)

    assert upload.file_path==file_path

    assert upload.user.gender=='female'
    assert upload.user.height==168.0
    assert upload.user.stride==70.0

    assert upload.trial.name=='walk1'
    assert upload.trial.rate==100
    assert upload.trial.steps==100

def test_all():
    uploads = Upload.all()

    assert len(uploads)>0
    assert map(lambda x: x.isinstance(Upload), uploads)

def test_generate_file_path():
    file_path = 'public/uploads/female-999-90_bagwalk1-89-10.txt'
    user = User('female', '999', '90')
    trial = Trial('bagwalk1', '89', '10')

    assert Upload.generate_file_path(user, trial)==file_path
