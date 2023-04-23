"""
You are given an array arr of n elements. In one operation you can pick two indices i and j, such that arr[i] >= arr[j] and replace the value of arr[i] with (arr[i] - arr[j]). You have to minimize the values of the array after performing any number of such operations.

Example 1:

Input:
n = 3
arr = {3,2,4}
Output:
1
Explanation:
1st Operation : We can pick 4 & 3, subtract 4-3 => {3,2,1}
2nd Opeartion : We can pick 3 & 2, subtarct 3-2 => {1,2,1}
3rd Operation : We can pick 1 & 2, subtract 2-1 => {1,1,1}
4th Opeartion : We can pick 1 & 1, subtract 1-1 => {1,0,1}
5th Operation : We can pick 1 & 1, subtract 1-1 => {0,0,1}
After this no operation can be performned, so maximum no is left in the array is 1, so the ans is 1.
Example 2:

Input:
n = 2
arr = {2,4}
Output:
2
Explanation:
1st Operation : We can pick 4 & 2, subtract 4-2 => {2,2}
2nd Operation : We can pick 2 & 2, subtract 2-2 => {0,2}
After this no operation can be performned, so maximum no is left in the array is 2, so the ans is 2.
"""

# My solution: -
class Solution:
    def minimumNumber(self, n, arr):
        while max(arr) != min(arr):
            max_index = arr.index(max(arr))
            min_index = arr.index(min(arr))
            arr[max_index] = arr[max_index] - arr[min_index]
        return max(arr)

# Testing
sol = Solution()

# Test Case 1
n1 = 3
arr1 = [3, 2, 4]
print(sol.minimumNumber(n1, arr1)) # Output: 1

# Test Case 2
n2 = 2
arr2 = [2, 4]
print(sol.minimumNumber(n2, arr2)) # Output: 2

# Another interesting solution I found: -
# This solution also reduces the time complexity ;)

from math import gcd

class Solution1:
    def minimumNumber1(self, n, arr):
        result = arr[0]
        for i in range(1, n):
            result = gcd(result, arr[i])
        return result

# Create an instance of the Solution class
solu = Solution1()

# Test Case 1
n3 = 3
arr3 = [3, 2, 4]
print(solu.minimumNumber1(n3, arr3)) # Output: 1

# Test Case 2
n4 = 2
arr4 = [2, 4]
print(solu.minimumNumber1(n4, arr4)) # Output: 2

