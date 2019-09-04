# Problem 1
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# 
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


def problem1(num_list, k):
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] + num_list[j] == k:
                return True
    return False

def test_should_return_true():
    num_list = [1, 2, 3]
    k = 5
    return problem1(num_list, k)

def test_should_return_false():
    num_list = [1, 2, 3]
    k = 6
    return problem1(num_list, k)

if __name__ == '__main__':
    print('Should return true:', test_should_return_true())
    print('Should return false:', test_should_return_false())