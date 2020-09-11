import pytest
from ..src.linked_list import *

def test_node():
    node = Node('abc')
    
    assert(node.data == 'abc')
    assert(node.next is None)


def test_linked_list_append():
    l = SinglyLinkedList()
    l.append('abc')
    l.append('def')
    
    assert(l.head.data == 'abc')
    assert(l.head.next.data == 'def')

def test_linked_list_delete():
    l = SinglyLinkedList()
    l.append('abc')
    l.delete('abc')

    assert(not l.contains('abc'))
    
    l = SinglyLinkedList()
    l.append('abc')
    l.append('def')
    l.delete('abc')

    assert(l.contains('def'))
    assert(not l.contains('abc'))

def test_linked_list_contains():
    l = SinglyLinkedList()
    l.append('abc')

    assert(l.contains('abc'))
    assert(not l.contains('def'))