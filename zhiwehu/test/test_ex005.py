from src.ex005 import *
import pytest

def test_string_holder():
    sh = StringHolder()
    sh.string = 'abcd'

    assert sh.uppercase_string() == 'ABCD'