# Problem 364
#   Medium
#   Asked by Facebook
#
# Describe an algorithm to compute the longest increasing subsequence of an array of 
#   numbers in O(n log n) time.
#

def longest_inc_subsequence(seq):
    if len(seq) in [0, 1]:
        return seq

    longest_begin, current_begin = 0, 0
    longest_length, current_length = 1, 1

    for i in range(len(seq)-1):
        if seq[i+1] > seq[i]:
            current_length += 1
        else:
            if current_length > longest_length:
                longest_begin = current_begin
                longest_length = current_length
            current_begin = i+1
            current_length = 1

    if current_length > longest_length:
        longest_begin = current_begin
        longest_length = current_length

    return seq[longest_begin : longest_begin + longest_length]


def test_longest_inc_subsequence():
    # Test strings
    assert(longest_inc_subsequence('') == '')
    assert(longest_inc_subsequence('1') == '1')
    assert(longest_inc_subsequence('12345') == '12345')

    assert(longest_inc_subsequence('54321') == '5')
    assert(longest_inc_subsequence('4321234') == '1234')

    # Test lists
    assert(longest_inc_subsequence([]) == [])
    assert(longest_inc_subsequence([1]))
    assert(longest_inc_subsequence([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])

    assert(longest_inc_subsequence([5, 4, 3, 2, 1]) == [5])
    assert(longest_inc_subsequence([4, 3, 2, 1, 2, 3, 4]) == [1, 2, 3, 4])


if __name__ == '__main__':
    test_longest_inc_subsequence()