from src.ex004 import *
import pytest

def test_num_list():
	num_input = '23,456,9,12,3'
	numbers = num_list(num_input)
	assert len(numbers) == 5
	assert type(numbers) == list
	assert numbers == ['23', '456', '9', '12', '3']

def test_num_tuple():
	num_list = ['23', '456', '9', '12', '3']
	numbers = num_tuple(num_list)
	assert len(numbers) == 5
	assert type(numbers) == tuple
	assert numbers == ('23', '456', '9', '12', '3')