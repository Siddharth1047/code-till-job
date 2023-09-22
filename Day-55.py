"""
You are given an array arr[] of N integers. The task is to find the smallest positive number missing from the array.
Note: Positive number starts from 1.

Example 1:
Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing 
number is 6.

Example 2:
Input:
N = 5
arr[] = {0,-10,1,3,-20}
Output: 2
Explanation: Smallest positive missing 
number is 2.
"""

def missing_value(arr):
    n = len(arr)
    b = arr
    hash = set(b)
    for i in range(1, n + 2):
        if i not in hash:
            return i
        
arr = [0, -10, 1, 3, -20]
print(missing_value(arr))