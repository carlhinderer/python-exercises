# Question 7
# Level 2
#
# Question:
#   Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in 
#    the i-th row and j-th column of the array should be i*j.
#
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
#
# Example:
#   Suppose the following inputs are given to the program:
#   3,5
#   Then, the output of the program should be:
#   [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
#
# Hints:
#   Note: In case of input data being supplied to the question, it should be assumed to be a console input in a 
#    comma-separated form.

def print_matrix():
    dimensions = get_dimensions()
    matrix = build_matrix(dimensions[0], dimensions[1])
    print(matrix)

def get_dimensions():
    dimensions = input('Enter the dimensions: ')
    return list(map(int, dimensions.split(',')))

def build_matrix(x, y):
    matrix = []
    for i in range(x):
        row = [i * j for j in range(y)]
        matrix.append(row)
    return matrix


if __name__ == '__main__':
    print_matrix()