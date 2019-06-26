from src.ex007 import *
import pytest

def test_build_matrix():
    matrix = build_matrix(3, 5)

    assert matrix[0] == [0, 0, 0, 0, 0]
    assert matrix[1] == [0, 1, 2, 3, 4]
    assert matrix[2] == [0, 2, 4, 6, 8]