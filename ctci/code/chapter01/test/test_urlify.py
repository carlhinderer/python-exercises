import pytest
from ..src.urlify import *

def test_urlify():
    assert(urlify('') == '')
    assert(urlify('abc') == 'abc')
    assert(urlify('Mr. John Smith') == 'Mr.%20John%20Smith')