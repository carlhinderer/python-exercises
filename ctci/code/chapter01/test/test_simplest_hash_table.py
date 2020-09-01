import pytest
from ..src.simplest_hash_table import *


def test_standard_hash_table():
    hash_table = StandardHashTable()
    hash_table.insert(10, 'China')

    assert(hash_table.search(10) == 'China')
    assert(hash_table.search(20) is None)

    hash_table.delete(10)
    assert(hash_table.search(10) is None)