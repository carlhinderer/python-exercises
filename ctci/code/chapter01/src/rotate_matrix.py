#
# 1.7 Rotate Matrix: 
#
# Given an image represented by an NxN matrix, where each pixel in the image is 
#   4 bytes, write a method to rotate the image by 90 degrees. Can you do this 
#   in place?
#

def rotate_matrix(m, clockwise=True):
    if clockwise:
        return rotate_clockwise(m)
    else:
        return rotate_counterclockwise(m)

def rotate_clockwise(m):
    rotated = []
    for i in range(len(m)):
        row = []
        for j in range(len(m)-1, -1, -1):
            row.append(m[j][i])
        rotated.append(row)
    return rotated

def rotate_counterclockwise(m):
    rotated = []
    for i in range(len(m)-1, -1, -1):
        row = []
        for j in range(len(m)):
            row.append(m[j][i])
        rotated.append(row)
    return rotated