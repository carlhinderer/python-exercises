from src.ex010 import *
import pytest

def test_sort_and_unique_words():
    words = ['hello', 'world', 'and', 'practice', 'makes', 'perfect', 
             'and', 'hello', 'world', 'again']
    sorted_and_unique = sort_and_unique_words(words)

    expected = ['again', 'and', 'hello', 'makes', 'perfect', 'practice', 'world']
    assert sorted_and_unique == expected