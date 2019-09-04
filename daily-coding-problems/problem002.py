# Problem 2
#
# Given an array of integers, return a new array such that each element at index i of the new array is 
#   the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If 
#   our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

def problem2(num_list):
    new_list = []
    for i in range(len(num_list)):
        product = 1
        for j in range(len(num_list)):
            if i != j:
                product *= num_list[j]
        new_list.append(product)
    return new_list

def test_empty_list():
    num_list = []
    result = problem2(num_list)
    print('Result should be empty list:', result)

def test_single_value_list():
    num_list = [4]
    result = problem2(num_list)
    print('Result should be a single 1:', result)

def test_multi_value_list():
    num_list = [1, 2, 3, 4, 5]
    result = problem2(num_list)
    print('Result should be [120, 60, 40, 30, 24]:', result)

if __name__ == '__main__':
    test_empty_list()
    test_single_value_list()
    test_multi_value_list()