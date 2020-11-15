#TODO: pytest or unittest?
from pydometer.models.filter import Filter

def test_filter_gravity():
    data = [0.123, 0.456, -0.212]
    expected = [0, 0, 7.109485333219216e-05]
    #TODO:
    # assert Filter.low_0_hz(data)==expected

def test_filter_smoothing():
    data = [0.0, 0.0, 0.0005219529804999682]
    expected = [0, 0, 4.9828746074755684e-05]
    #TODO:
    # assert Filter.low_5_hz(data)==expected

def test_filter_highpass():
    data = [0, 0, 4.9828746074755684e-05]
    expected = [0, 0, 4.753597533351234e-05]
    #TODO:
    # assert Filter.high_1_hz(data)==expected
