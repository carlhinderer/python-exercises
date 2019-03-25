from src.ex001 import *
import pytest

def test_div_7_not_5():
	numbers = div_7_not_5()
	first_value = numbers[0]
	last_value = numbers[-1]

	assert first_value >= 2000
	assert first_value % 7 == 0
	
	assert last_value <= 3200
	assert last_value % 7 == 0

	for i in range(10): 
		assert numbers[i] % 5 != 0