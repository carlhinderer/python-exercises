import pytest
from ..src.linked_list import *

def test_node():
    node = Node('abc')
    
    assert(node.data == 'abc')

def test_linked_list_append():
    l = SinglyLinkedList()
    l.append('abc')
    l.append('def')
    
    assert(l.head.data == 'abc')
    assert(l.head.next.data == 'def')