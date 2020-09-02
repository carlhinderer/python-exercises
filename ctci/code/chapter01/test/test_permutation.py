import pytest
from ..src.permutation import *

def test_permutation():
    assert(permutation('', ''))
    assert(permutation('abc', 'cba'))

    assert(not permutation('', 'a'))
    assert(not permutation('aa', 'ab'))
    assert(not permutation('abc', 'a'))