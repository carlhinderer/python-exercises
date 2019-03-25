# Question 4
# Level 1
#
# Question:
# Write a program which accepts a sequence of comma-separated numbers 
#   from console and generate a list and a tuple which contains every number.
#   Suppose the following input is supplied to the program:
#   34,67,55,33,12,98
#
# Then, the output should be:
#   ['34', '67', '55', '33', '12', '98']
#   ('34', '67', '55', '33', '12', '98')

def get_input():
	return input('Enter a comma-separated list of numbers: ')

def num_list(input_nums):
	return input_nums.split(',')

def num_tuple(input_list):
	return tuple(input_list)

def print_list_and_tuple():
    input_nums = get_input()
    input_list = num_list(input_nums)
    print(input_list)
    print(num_tuple(input_list))


if __name__ == '__main__':
    print_list_and_tuple()
