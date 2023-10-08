# Find transpose of a Matrix (Convert all rows to columns and columns to rows)

def Transpose(matrix, n):
    for i in range(n):
        for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix

arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

n = 4
print(Transpose(arr,n))

"""
Given a square matrix of size N x N. The task is to rotate it by 
90 degrees in anti-clockwise direction without using any extra space. 

Example 1:
Input:
N = 3 
matrix[][] = {{1, 2, 3},
              {4, 5, 6}
              {7, 8, 9}}
Output: 
Rotated Matrix:
3 6 9
2 5 8
1 4 7

Example 2:
Input:
N = 2
matrix[][] = {{1, 2},
              {3, 4}}
Output: 
Rotated Matrix:
2 4
1 3
"""

def rotateby90(a, n):
    for i in range(0, len(a)):
        a[i] = a[i][::-1]
    
    for i in range(0, n):
        for j in range(i + 1, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]

    return a

a = [[1,2],[3,4]]
o = 2
print(rotateby90(a, o))

     