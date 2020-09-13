from ..src.queue import *
import pytest

def test_enqueue_dequeue():
    q = Queue()
    with pytest.raises(QueueEmptyError):
        q.dequeue()

    q.enqueue('abc')
    q.enqueue('def')
    assert(q.dequeue() == 'abc')
    assert(q.dequeue() == 'def')

    with pytest.raises(QueueEmptyError):
        q.dequeue()

def test_peek():
    q = Queue()
    with pytest.raises(QueueEmptyError):
        q.peek()

    q.enqueue('abc')
    q.enqueue('def')
    assert(q.peek() == 'abc')
    assert(q.peek() == 'abc')

def test_is_empty():
    q = Queue()
    assert(q.is_empty())

    q.enqueue('abc')
    assert(not q.is_empty())