"""
Question: Find the total number of vowels in all possible substring of a string.

Example:
Input: "abc"
Output: 3

Explanation: string 'abc' has 'a', 'b', 'c', 'ab', 'bc', 'abc' as it's 
substrings and vowel 'a' occurs 3 times in all substrings combined
"""

def subString(string):
    n = len(string)
    total_count = 0
    string = string.lower()
    vowels = "aeiou"

    for i in range(n):
        for j in range(i, n):
            substring = string[i:j+1]
            vowel_count = sum(1 for char in substring if char in vowels)

            total_count += vowel_count

    return total_count

string = "daceh"
print(subString(string))

string2 = "abc"
print(subString(string2))