"""
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
Example 1:

Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation: 
arr[0] + arr[1] = 1 + 5 = 6 
and arr[1] + arr[3] = 5 + 1 = 6.

Example 2:

Input:
N = 4, K = 2
arr[] = {1, 1, 1, 1}
Output: 6
Explanation: 
Each 1 will produce sum 2 with any 1.
"""
class Solution:
    def getPairsCount(self, arr, n, k):
        count = 0
        freq = {}
        for i in range(n):
            if arr[i] not in freq:
                freq[arr[i]] = 0
            freq[arr[i]] += 1
        for i in range(n):
            if k - arr[i] in freq:
                count += freq[k - arr[i]]
            if k - arr[i] == arr[i]:
                count -= 1
        return count // 2

# Create an instance of the Solution class
sol = Solution()

# Test Case 1
arr1 = [1, 5, 7, 1]
n1 = len(arr1)
k1 = 6
print(sol.getPairsCount(arr1, n1, k1)) # Output: 2

# Test Case 2
arr2 = [1, 1, 1, 1]
n2 = len(arr2)
k2 = 2
print(sol.getPairsCount(arr2, n2, k2)) # Output: 6

"""
Given an array arr of size N, the task is to count the number of elements of the array which are Fibonacci numbers

Example 1:
Input: N = 9, arr[] = {4, 2, 8, 5, 20, 1, 40, 13, 23}
Output: 5
Explanation: Here, Fibonacci series will 
be 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55. 
Numbers that are present in array are 
2, 8, 5, 1, 13

Example 2:
Input: N = 4, arr[] = {4, 7, 6, 25} 
Output: 0
Explanation: No Fibonacci number in 
this array.
"""

def fibo_search(arr):
    max_num = max(arr)

    fibo = [0,1]
    while fibo[-1] <= max_num:
        fibo.append(fibo[-1] + fibo[-2])

    fibo_set = set(fibo)

    count = 0
    for num in arr:
        if num in fibo_set:
            count += 1

    return count

arr = [4, 2, 8, 5, 20, 1, 40, 13, 23]
result = fibo_search(arr)
print(result)
