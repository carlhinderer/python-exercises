from src.ex008 import *
import pytest

def test_sort_words():
    words = ['without', 'hello', 'bag', 'world']
    sorted_words = sort_words(words)

    assert sorted_words == ['bag', 'hello', 'without', 'world']