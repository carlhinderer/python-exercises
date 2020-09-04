import pytest
from ..src.string_rotation import *

def test_string_rotation():
    assert(is_rotation('', ''))
    assert(is_rotation('a', 'a'))
    assert(is_rotation('abc', 'abc'))
    assert(is_rotation('waterbottle', 'erbottlewat'))

    assert(not is_rotation('', 'a'))
    assert(not is_rotation('abcde', 'bcbea'))