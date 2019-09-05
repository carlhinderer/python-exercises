# Problem 4
#
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other 
#   words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and 
#   negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

def lowest_positive_integer(num_list):
    num_list[:] = [n for n in num_list if n > 0]
    return max_number_space(num_list)

def max_number_space(num_list):
    max_num = max(num_list)
    if max_num < 0:
        return 1
    positives = [0] * max_num
    for i in range(len(num_list)):
        if positives[num_list[i] - 1] == 0:
            positives[num_list[i] - 1] = 1
    for i in range(len(positives)):
        if positives[i] == 0:
            return i + 1
    return max_num + 1

if __name__ == '__main__':
    num_list = [3, 4, -1, 1]
    result = lowest_positive_integer(num_list)
    print('Result:', result)