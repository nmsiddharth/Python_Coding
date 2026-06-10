input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Method 1

# def check(input):
#     n = len(input)
#     # Transpose the matrix
#     for i in range(n):
#         for j in range(i,n):
#             input[i][j], input[j][i] = input[j][i], input[i][j]
            
#     # reverse a row
#     for i in input:
#         i.reverse()
    
#     print(input)
    
# check(input)

# Method 2 using Numpy
import numpy as np

def check(input):
    arr = np.array(input)
    arr_T = arr.T
    print(arr_T)
    arr_rev = np.fliplr(arr_T)
    print(arr_rev)
check(input)                    