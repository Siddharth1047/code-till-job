# 2D Arrays
a_2d = [[1,2,3],
        [5,6,7]]
print("2D Array is", a_2d)

# Replace 6 with 99
b_2d = [[1,2,3],[5,6,7]]
b_2d[1][1] = 99
print(b_2d[1])

# Print the whole 2D array
c_2d = [['x','y','z'],['a','b','c']]
for letter in c_2d:
  for num in letter:
    print(num)

# Another way
for i in range(len(c_2d)):
  for j in range(len(c_2d[i])):
    print(c_2d[i][j])

# Sum of diagonals in a 2D array
diag = [[1,2,3],
        [4,5,6],
        [7,8,9]]

def diagonal_sum(arr):
  total = 0
  for i in range(len(diag)):
    total += arr[i][i]
  return total
return_sum = print(diagonal_sum(diag))
print("Diagonal sum is: -", return_sum)

# Rooks are safe problem
def rooks_are_safe(chess):
  n = len(chess)
  for row_i in range(n):
    row_count = 0
    for col_i in range(n):
      row_count += chess[row_i][col_i]
    if row_count > 1:
      return False
  for col_i in range(n):
    col_count = 0
    for row_i in range(n):
      col_count += chess[row_i][col_i]
    if col_count > 1:
      return False
  return True

rooks = [[1,0,0,0],
         [0,1,0,0],
         [0,0,0,1],
         [0,0,0,0]]
print(rooks_are_safe(rooks))
