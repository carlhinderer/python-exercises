import pytest
from ..src.linked_list import *
from ..src.remove_duplicates import *

def test_remove_dups():
    ll = SinglyLinkedList()
    ll.append('abc')
    ll.append('def')
    ll.append('abc')
    ll.append('abc')

    remove_dups(ll)

    assert(ll.head.data == 'abc')
    assert(ll.head.next.data == 'def')
    assert(ll.head.next.next is None)


def test_remove_dups_no_buffer():
    pass