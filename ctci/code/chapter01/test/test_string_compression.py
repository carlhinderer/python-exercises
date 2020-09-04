import pytest
from ..src.string_compression import *

def test_compress():
    assert(compress('') == '')
    assert(compress('a') == 'a1')
    assert(compress('aaabbbcccaaa') == 'a3b3c3a3')

def test_smallest_string():
    assert(smallest_string('') == '')
    assert(smallest_string('a') == 'a')
    assert(smallest_string('aaa') == 'a3')