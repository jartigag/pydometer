import pytest

from pydometer.models.trial import Trial

def test_create():
    trial = Trial('walk 1 ', 5, '10')

    assert trial.name=='walk1'
    assert trial.rate==5
    assert trial.steps==10

@pytest.mark.parametrize("name", [None, '', ' '])
def test_create_empty_name(name):
    with pytest.raises(ValueError) as e:
        Trial(name)
    assert str(e.value)=="Invalid name"

@pytest.mark.parametrize("rate", [0, '0', -1, '-1', 'invalid rate', 2.5, '2.5'])
def test_create_with_rate(rate):
    assert Trial('walk1').rate==None
    assert Trial('walk1', rate=None).rate==None
    assert Trial('walk1', rate='').rate==None

    with pytest.raises(ValueError) as e:
        Trial('walk1', rate=rate)
    assert str(e.value)=="Invalid rate"

@pytest.mark.parametrize("steps", [-1, '-1', 'invalid steps', 2.5, '2.5'])
def test_create_with_steps(steps):
    assert Trial('walk1').steps==None
    assert Trial('walk1', steps=None).steps==None
    assert Trial('walk1', steps='').steps==None

    with pytest.raises(ValueError) as e:
        Trial('walk1', steps=steps)
    assert str(e.value)=="Invalid steps"

def test_create_with_steps():
    assert Trial('walk1', None, 0).steps==0
    assert Trial('walk1', None, '0').steps==0
    assert Trial('walk1', None, 1).steps==1
    assert Trial('walk1', None, '1').steps==1
    assert Trial('walk1', None, 100).steps==100
    assert Trial('walk1', None, '100').steps==100
