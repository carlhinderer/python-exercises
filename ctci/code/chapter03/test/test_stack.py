from ..src.stack import *
import pytest

def test_push_pop():
    s = Stack()
    with pytest.raises(StackEmptyError):
        s.pop()

    s.push('abc')
    s.push('def')
    assert(s.pop() == 'def')
    assert(s.pop() == 'abc')

    with pytest.raises(StackEmptyError):
        s.pop()

def test_peek():
    s = Stack()
    with pytest.raises(StackEmptyError):
        s.peek()

    s.push('abc')
    assert(s.peek() == 'abc')

def test_is_empty():
    s = Stack()
    assert(s.is_empty())

    s.push('abc')
    assert(not s.is_empty())