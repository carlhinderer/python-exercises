import pytest
from ..src.unique import *

def test_unique_with_set():
    assert(unique_with_set(''))
    assert(unique_with_set('a'))
    assert(unique_with_set('abcd'))

    assert(not unique_with_set('aa'))
    assert(not unique_with_set('abcda'))

def test_unique_with_stack():
    assert(unique_with_stack(''))
    assert(unique_with_stack('a'))
    assert(unique_with_stack('abcd'))

    assert(not unique_with_stack('aa'))
    assert(not unique_with_stack('abcda'))