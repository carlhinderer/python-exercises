import pytest
from ..src.zero_matrix import *

def test_zero_matrix():
    # No zeros
    M = [[1, 2],
         [3, 4]]
    assert(zero_matrix(M) == M)

    # With one zero
    M = [[1, 2, 0],
         [4, 5, 6],
         [7, 8, 9]]
    M_zeroed = [[0, 0, 0], 
                [4, 5, 0],
                [7, 8, 0]]
    assert(zero_matrix(M) == M_zeroed)

    # With multiple zeros
    M = [[1, 2, 0],
         [4, 5, 6],
         [0, 8, 9]]
    M_zeroed = [[0, 0, 0], 
                [0, 5, 0],
                [0, 0, 0]]
    assert(zero_matrix(M) == M_zeroed)