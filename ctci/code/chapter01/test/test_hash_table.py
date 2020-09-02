import pytest
from ..src.hash_table import *

def test_setitem():
    ht = HashTable()

    ht['foo'] = 'bar'
    assert(ht['foo'] == 'bar')

    ht['foo'] = 'baz'
    assert(ht['foo'] == 'baz')


def test_getitem():
    ht = HashTable()

    ht['foo'] = 'bar'
    assert(ht['foo'] == 'bar')

    with pytest.raises(KeyError):
        ht['baz']
