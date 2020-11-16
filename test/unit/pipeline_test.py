import pytest

from pydometer.models.pipeline import Pipeline
from pydometer.models.user import User
from pydometer.models.trial import Trial

def test_new_combined_data():
    file_path = 'test/data/female-167-70_bagwalk1-100-10.txt'
    user = User()
    trial = Trial('foobar1', 100)
    pipeline = Pipeline(open(file_path).read(), user, trial)

    assert user==pipeline.user
    assert trial==pipeline.trial
    assert pipeline.parser
    assert pipeline.processor
    assert pipeline.analyzer

    assert pipeline.analyzer.steps==12
    assert pipeline.analyzer.distance==888.0
    assert pipeline.analyzer.time==8

def test_new_separated_data():
    file_path = 'test/data/female-167-70_bagwalk2-100-10.txt'
    user = User()
    trial = Trial('foobar1', 100)
    pipeline = Pipeline(open(file_path).read(), user, trial)

    assert user==pipeline.user
    assert trial==pipeline.trial
    assert pipeline.parser
    assert pipeline.processor
    assert pipeline.analyzer

    assert pipeline.analyzer.steps==12
    assert pipeline.analyzer.distance==888.0
    assert pipeline.analyzer.time==9
