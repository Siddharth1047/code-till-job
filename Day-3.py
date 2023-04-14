"""
Given a string S consisting of lowercase Latin Letters. Return the first non-repeating character in S. If there is no non-repeating character, return '$'.
Example 1:
Input:
S = hello
Output: h
Explanation: In the given string, the
first character which is non-repeating
is h, as it appears first and there is
no other 'h' in the string.
Example 2:

Input:
S = zxvczbtxyzvy
Output: c
Explanation: In the given string, 'c' is
the character which is non-repeating.
"""
def check(s):
    
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
    count1 = []
    for j in count:
        if count[j] == 1:
            count1.append(j)
    
    if len(count1) <= 0:
        print('$')
    else:
        print(count1[0])
check('hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs')
check('zxvczbtxyzvy')
check('ddhh')