# Problem 446
#   Medium
#   Asked by Indeed
#
# Given a 32-bit positive integer N, determine whether it is a power of 
#   four in faster than O(log N) time.
#

def is_power_of_4(N):
    bin_num = '{0:b}'.format(N)
    first, rest = bin_num[0], bin_num[1:]
    if first != '1':
        return False
    return (len(rest) % 2 == 0) and (not '1' in rest)

def test_is_power_of_4():
    assert is_power_of_4(1)
    assert is_power_of_4(4)
    assert is_power_of_4(16)
    assert is_power_of_4(64)

    assert not is_power_of_4(0)
    assert not is_power_of_4(2)
    assert not is_power_of_4(15)

if __name__ == '__main__':
    test_is_power_of_4()

# Running Time
#   If N = 4**a,
#   O(2a) = O(a)