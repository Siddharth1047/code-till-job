"""
You're given a string, replace all the vowels in that string with underscore(_).

Constraint 1:  
Replace the vowel based on it's position in string.
Example: If vowel is at 2nd position then replace that vowel with 2 underscores,
if the position is at 3rd index then replace with 3 underscores.

Constraint 2: 
Maximum number of underscores which can be replaced is 5.
Example: If the position of a vowel is 7, then replace it with 5 underscores.

Example 1:
String = "VOWEL"
Output: "V__W____L"

Example 2:
String = "DELETE"
Output: "D__L____T_____"
"""

def underScore(string):
    vowels = "AEIOU"
    string = string.upper()
    underscore_count = 0
    arr = []

    for i, char in enumerate(string):
        if char in vowels:
            underscore_count = min(i + 1, 5) # "i + 1" because indexing starts from 0 in python
            arr.append('_' * underscore_count)
        else:
            arr.append(char)

    return ''.join(arr) # convert the array into string

str1 = "vowel"
str2 = "delete"

print(f"Original string was '{str1}', and the output string is {underScore(str1)}")
print(f"Original string was '{str2}', and the output string is {underScore(str2)}")