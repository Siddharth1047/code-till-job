"""
Given two numbers 'N' and 'S' , find the largest number that can be formed with 'N' digits and whose sum of digits should be equals to 'S'. 
Return -1 if it is not possible.

Example 1:
Input: N = 2, S = 9
Output: 90
Explaination: It is the biggest number 
with sum of digits equals to 9.

Example 2:
Input: N = 3, S = 20
Output: 992
Explaination: It is the biggest number 
with sum of digits equals to 20.
"""

def largestNumber(N, S):
    # input validation check if it's possible to create a number with the sum of S as 9 is the largest single digit int
    if S > 9 * N or (S == 0 and N > 1):
        return -1
    
    result = ""

    while N > 0:
        digit = min(9, S) # take minimum between 9 and S
        result += str(digit) # add to result

        S -= digit
        N -= 1

    return int(result)

print(largestNumber(2, 9))
print(largestNumber(3, 20))