import pytest
from ..src.palindrome_permutation import *

def test_palindrome_permutation():
    assert(palindrome_permutation(''))
    assert(palindrome_permutation('a'))
    assert(palindrome_permutation('aba'))
    assert(palindrome_permutation('taco cat'))

    assert(not palindrome_permutation('abc'))
    assert(not palindrome_permutation('abcbba'))