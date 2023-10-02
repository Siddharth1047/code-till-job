"""
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example 1:
Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole
string(not individual words), the input
string becomes
much.very.program.this.like.i

Example 2:
Input:
S = pqr.mno
Output: mno.pqr
Explanation: After reversing the whole
string , the input string becomes
mno.pqr
"""

def reverseString(S):
    words = S.split('.')
    words.reverse()
    reversed_string = '.'.join(words)
    return reversed_string

S = "i.love.python.programming"
print(reverseString(S))

"""
Find the greatest number in a string

Example:
Input: "exgr69urh9k2"
Output: 69
"""

import re 
def largestNumber(string):
    numbers = re.findall(r"\d+", string)

    if numbers:
        return max(numbers, key = int)
    else:
        return None
    
string = "agsdjh4543sdldh213"
print(largestNumber(string))