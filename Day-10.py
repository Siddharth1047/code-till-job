# Binary Search.

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1 # if not found return -1

print(binary_search([1,2,3,4,5],5))
print(binary_search([12,52,73,44,50],5))

"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""

# use binary search to find square root

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        left = 0
        right = x
        
        while left < right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid

        return left - 1
    
# Driver code
sol = Solution()

# Test cases
print(sol.mySqrt(81))  # Output: 9
print(sol.mySqrt(169))  # Output: 13
print(sol.mySqrt(0))  # Output: 0
print(sol.mySqrt(3025))  # Output: 55
print(sol.mySqrt(90))  # Output: 9
