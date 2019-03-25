from src.ex002 import *
import pytest

def test_factorial():
	assert factorial(0) == 1
	assert factorial(1) == 1
	assert factorial(2) == 2
	assert factorial(3) == 6