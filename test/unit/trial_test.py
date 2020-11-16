import pytest

from pydometer.models.trial import Trial

def test_create():
    trial = Trial('walk 1 ', 5, '10')

    assert trial.name=='walk1'
    assert trial.rate==5
    assert trial.steps==10

def test_create_empty_name():
    pass #TODO

def test_create_with_rate():
    pass #TODO

def test_create_with_steps():
    pass #TODO
