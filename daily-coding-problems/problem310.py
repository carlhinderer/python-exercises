# Problem 310
#   Easy
#   Asked by Pivotal
#
# Write an algorithm that finds the total number of set bits in all integers between 
#   1 and N.
#


def total_number_set_bits(N):
    total_bits = 0
    for num in range(1, N+1):
        total_bits += set_bits_in_number(num)
    return total_bits

def set_bits_in_number(N):
    binary = bin(N)[2:]
    return binary.count('1')


def test_problem_310():
    assert total_number_set_bits(0) == 0
    assert total_number_set_bits(1) == 1
    assert total_number_set_bits(2) == 2
    assert total_number_set_bits(3) == 4
    assert total_number_set_bits(4) == 5

if __name__ == '__main__':
    test_problem_310()