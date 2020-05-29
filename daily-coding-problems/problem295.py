# Problem295
#   Medium
#   Asked by Stitch Fix
#
# Pascal's triangle is a triangular array of integers constructed with the 
#   following formula:
#
#      The first row consists of the number 1.
#
#      For each subsequent row, each element is the sum of the numbers directly 
#         above it, on either side.
#
# For example, here are the first few rows:
#
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
#
# Given an input k, return the kth row of Pascal's triangle.
#
# Bonus: Can you do this using only O(k) space?
#

def pascal_triangle_row(k):
    current_row = [1]
    for i in range(k-1):
        new_row = []
        new_row.append(1)
        for j in range(len(current_row) - 1):
            new_row.append(current_row[j] + current_row[j+1])
        new_row.append(1)
        current_row = new_row     
    return current_row

def print_row(row):
    for i in range(len(row)):
        print(row[i], end=' ')
    print('\n')

def test_pascal_triangle(num_rows):
    for i in range(1, num_rows + 1):
        print('k=%s' % i)
        print_row(pascal_triangle_row(i))

if __name__ == '__main__':
    test_pascal_triangle(5)