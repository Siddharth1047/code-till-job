"""
This is a comment: -
Q-1- Write a code where: Given an array A of n positive numbers. The task is to find the first Equilibrium Point in an array. 
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

Note: Retun the index of Equilibrium point. (1-based index)

Example 1:

Input: 
n = 5 
A[] = {1,3,5,2,2} 
Output: 3 
Explanation:  
equilibrium point is at position 3 
as elements before it (1+3) = 
elements after it (2+2)

"""
def equilibrium(arr):
    n = len(arr)

    for i in range(n):
        leftsum = 0
        rightsum = 0

        for j in range(i):
            leftsum += arr[j]

        for j in range(i+1, n):
            rightsum += arr[j]

        if leftsum == rightsum:
            return i
    return False

arr = [1,3,5,2,2]
print(equilibrium(arr))