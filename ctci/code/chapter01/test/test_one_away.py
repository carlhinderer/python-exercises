import pytest
from ..src.one_away import *

def test_one_away():
    # Zero away
    assert(one_away('', ''))
    assert(one_away('abc', 'abc'))

    # One away
    # assert(one_away('a', 'ab'))
    # assert(one_away('a', ''))

    # More than one away
    # assert(not one_away('', 'ab'))
    # assert(not one_away('a', 'abc'))