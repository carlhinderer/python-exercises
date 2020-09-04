#
# 1.8 Zero Matrix: 
#
# Write an algorithm such that if an element in an MxN matrix is 0, its entire 
#   row and column are set to O. 
#

def zero_matrix(M):
    rows_with_zeros = []
    columns_with_zeros = []
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == 0:
                rows_with_zeros.append(i)
                columns_with_zeros.append(j)
    for i in range(len(M)):
        for j in range(len(M[i])):
            if i in rows_with_zeros or j in columns_with_zeros:
                M[i][j] = 0
    return M