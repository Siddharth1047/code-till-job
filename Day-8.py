class Solution:
    def commonElements(self, A, B, C, n1, n2, n3):
        p1, p2, p3 = 0, 0, 0
        common_elements = []  

        while p1 < n1 and p2 < n2 and p3 < n3:
            if A[p1] == B[p2] == C[p3]:
                if not common_elements or common_elements[-1] != A[p1]:
                    common_elements.append(A[p1])
    
                p1 += 1
                p2 += 1
                p3 += 1

            elif A[p1] < B[p2]:
                p1 += 1
            elif B[p2] < C[p3]:
                p2 += 1
            else:
                p3 += 1
        return common_elements

# Example usage
A = [1, 5, 10, 20, 40, 80,120]
B = [6, 7, 20, 80, 120]
C = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(A)
n2 = len(B)
n3 = len(C)

# Create an object of Solution class
sol = Solution()
# Call the commonElements method
common_elements = sol.commonElements(A, B, C, n1, n2, n3)
print(common_elements)  

"""
Given a non-negative integer N. The task is to check if N is a power of 2. More formally, check if N can be expressed as 2x for some x.

Example 1:

Input: N = 1
Output: YES
Explanation:1 is equal to 2 
raised to 0 (20 = 1).
Example 2:

Input: N = 98
Output: NO
Explanation: 98 cannot be obtained
by any power of 2.
"""
# This was an interesting problem to solve as I had no idea how to use bitwise operators in python

def power2(n):

    if n == 0:
        return False
    else:
        return (n & (n - 1)) == 0
    
n1 = 2
n2 = 98
n3 = 256
n4 = 16
print(power2(n1))
print(power2(n2))
print(power2(n3))
print(power2(n4))