import pytest
from ..src.permutation import *

def test_permutation():
    assert(permutation('abc', 'cba'))
    assert(not permutation('aa', 'ab'))