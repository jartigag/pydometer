import pytest

from pydometer.helpers.view_helper import ViewHelper

def test_format_distance():
    assert  '0.01 cm'==ViewHelper.format_distance(0.01)
    assert  '1.00 cm'==ViewHelper.format_distance(1)
    assert '99.99 cm'==ViewHelper.format_distance(99.987)

    assert   '1.00 m'==ViewHelper.format_distance(99.999)
    assert   '1.00 m'==ViewHelper.format_distance(100)
    assert '999.99 m'==ViewHelper.format_distance(99998.99)

    assert  '1.00 km'==ViewHelper.format_distance(99999.99)
    assert  '1.00 km'==ViewHelper.format_distance(100000)
    assert  '1.99 km'==ViewHelper.format_distance(199000)

def test_format_time_none():
    assert None==ViewHelper.format_distance('')

def test_format_time():
    assert '0 hr, 0 min, 1 sec'==ViewHelper.format_time(1)
    assert '0 hr, 0 min, 59 sec'==ViewHelper.format_time(59.4)
    assert '0 hr, 1 min, 0 sec'==ViewHelper.format_time(59.9)
    assert '0 hr, 1 min, 0 sec'==ViewHelper.format_time(60)
    assert '0 hr, 59 min, 59 sec'==ViewHelper.format_time(3599.4)
    assert '1 hr, 0 min, 0 sec'==ViewHelper.format_time(3599.9)
    assert '1 hr, 0 min, 0 sec'==ViewHelper.format_time(3600)
    assert '1 hr, 5 min, 0 sec'==ViewHelper.format_time(3900)
    assert '17 hr, 46 min, 39 sec'==ViewHelper.format_time(9999999999)

def test_limit_1000_series_none():
    assert ViewHelper.limit_1000(None)==[]

def test_limit_1000_series_empty():
    assert ViewHelper.limit_1000([])==[]

def test_limit_1000_series_500():
    series = range(0,500)
    assert ViewHelper.limit_1000(series)==series

def test_limit_1000_series_2000():
    series = range(0,2000)
    assert ViewHelper.limit_1000(series)==series[:999]
