import pytest
from ..src.rotate_matrix import *

TEST_MATRIX_3 = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

TEST_MATRIX_4 = [[1, 2, 3, 4],
                 [5, 6, 7, 8], 
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]]

CLOCKWISE_ROTATED_3 = [[7, 4, 1],
                       [8, 5, 2],
                       [9, 6, 3]]

COUNTER_ROTATED_3 = [[3, 6, 9],
                     [2, 5, 8],
                     [1, 4, 7]]

CLOCKWISE_ROTATED_4 = [[13, 9, 5, 1],
                       [14, 10, 6, 2], 
                       [15, 11, 7, 3],
                       [16, 12, 8, 4]]

COUNTER_ROTATED_4 = [[4, 8, 12, 16], 
                     [3, 7, 11, 15], 
                     [2, 6, 10, 14], 
                     [1, 5, 9, 13]]

def test_rotate_matrix():
    # Clockwise
    assert(rotate_matrix(TEST_MATRIX_3) == CLOCKWISE_ROTATED_3)
    assert(rotate_matrix(TEST_MATRIX_4) == CLOCKWISE_ROTATED_4)

    # Counterclockwise
    assert(rotate_matrix(TEST_MATRIX_3, False) == COUNTER_ROTATED_3)
    assert(rotate_matrix(TEST_MATRIX_4, False) == COUNTER_ROTATED_4)

    # Both
    clockwise_first_3 = rotate_matrix(rotate_matrix(TEST_MATRIX_3), False)
    clockwise_first_4 = rotate_matrix(rotate_matrix(TEST_MATRIX_4), False)
    assert(clockwise_first_3 == TEST_MATRIX_3)
    assert(clockwise_first_4 == TEST_MATRIX_4)

    counter_first_3 = rotate_matrix(rotate_matrix(TEST_MATRIX_3, False))
    counter_first_4 = rotate_matrix(rotate_matrix(TEST_MATRIX_4, False))
    assert(counter_first_3 == TEST_MATRIX_3)
    assert(clockwise_first_4 == TEST_MATRIX_4)