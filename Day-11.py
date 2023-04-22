"""
You are given an array arr of n integers. For each index i, you have to find the sum of all integers present in the array with a value less than arr[i].
Example 1:

Input:
n = 3
arr = {1, 2, 3}
Output:
0 1 3
Explanation:
For 1, there are no elements lesser than itself.
For 2, only 1 is lesser than 2.
And for 3, 1 and 2 are lesser than 3, so the sum is 3.
Example 2:

Input:
n = 2
arr = {4, 4}
Output:
0 0
Explanation:
For 4, there are no elements lesser than itself. 
For 4, there are no elements lesser than itself.
There are no smaller elements than 4.
"""

# My solution: -
from typing import List

class Solution:
    def smallerSum(self, n: int, arr: List[int]) -> List[int]:
        result = []
        for i in range(n):
            sum = 0
            for j in range(n):
                if arr[j] < arr[i]:
                    sum += arr[j]
            result.append(sum)
        return result
    
# Example input
n = 5
arr = [3, 5, 1, 8, 9]
    
sol = Solution()
output = sol.smallerSum(n, arr)
print("Input array:", arr)
print("Smaller sum for each element:", output)

# Another interesting solution I found for this is: -

from typing import List

class Solution1:
    def smallerSum1(self, n: int, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        prefix_sum = [0]
        for num in sorted_arr:
            prefix_sum.append(prefix_sum[-1] + num)
        result = []
        for num in arr:
            index = self.binary_search(sorted_arr, num)
            result.append(prefix_sum[index])
        return result
        
    def binary_search(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

# Example input
n = 5
arr = [3, 5, 1, 8, 9]
    
sol = Solution1()
output = sol.smallerSum1(n, arr)
print("Input array:", arr)
print("Smaller sum for each element:", output)