# Given a string remove all the vowels which are in between 2 consonants
# Example:- string = "bobbaa"
# Output:- "bbbaa"

def sandwich(string):
    arr = list(string)
    n = len(arr)

    i = 1
    vowels = ['a','e','i','o','u','A','E','I','O','U']

    while i < n - 1:
        if arr[i] in vowels and arr[i - 1] not in vowels and arr[i + 1] not in vowels:
            arr.pop(i)
            n -= 1
        else:
            i += 1
    
    return ''.join(arr)

string = "yksbicebeunhkyzwjb"
print(sandwich(string))