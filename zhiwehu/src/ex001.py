# Question 1
# Level 1
#
# Question:
# Write a program which will find all such numbers which are divisible 
#   by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
#   The numbers obtained should be printed in a comma-separated sequence on 
#   a single line.

LOWER_BOUND = 2000
UPPER_BOUND = 3200

def div_7_not_5():
    num_range = range(LOWER_BOUND, UPPER_BOUND+1)
    return [i for i in num_range if (i % 7 == 0) and (i % 5 != 0)]


if __name__ == '__main__':
    for i in div_7_not_5():
    	print(i)