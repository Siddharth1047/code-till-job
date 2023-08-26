# Three great candidates
"""
The hiring team aims to find 3 candidates who are great collectively. Each candidate has his or her ability expressed as an integer. 3 candidates are great collectively if product of their abilities is maximum. Given abilities of N candidates in an array arr[], find the maximum collective ability from the given pool of candidates.

Example 1:
Input:
N = 5
Arr[] = {10, 3, 5, 6, 20}
Output: 1200
Explanation:
Multiplication of 10, 6 and 20 is 1200.

Example 2:
Input:
N = 5
Arr[] = {-10, -3, -5, -6, -20}
Output: -90
Explanation:
Multiplication of -3, -5 and -6 is -90.
"""
def maxCandidates(arr,n):
    if n < 3:
        return -1
    
    arr.sort()
    return max(arr[0] * arr[1] * arr[n-1], arr[n-1] * arr[n-2] * arr[n-3])

arr = [10,3,5,6,20]
n = len(arr)
print(maxCandidates(arr,n))
# Hint: Sometimes product of 2 negative integers can be a positive integer which is greater than the initial 2 largest integers