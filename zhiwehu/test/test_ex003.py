from src.ex003 import *
import pytest

def test_numbers_and_squares():
    d = numbers_and_squares(1)
    assert len(d) == 1
    assert d[1] == 1

    d = numbers_and_squares(2)
    assert len(d) == 2
    assert d[2] == 4