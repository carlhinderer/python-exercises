from src.ex006 import *
import pytest

def test_transform_number():
    t1 = transform_number(100)
    t2 = transform_number(150)
    t3 = transform_number(180)

    assert t1 == 18
    assert t2 == 22
    assert t3 == 24