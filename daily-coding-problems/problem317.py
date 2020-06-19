# Problem 317
#   Medium
#   Asked by Yahoo
#
# Write a function that returns the bitwise AND of all integers between M and N, 
#   inclusive.
#

import functools

def bitwise_and_for_range(m, n):
    numbers = range(m, n+1)
    return functools.reduce(lambda a, b: a & b, numbers)


if __name__ == '__main__':
    result = bitwise_and_for_range(50, 55)
    print('Result: ', result)