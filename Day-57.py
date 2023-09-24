"""
GFG POTD (24-09-2023)
Given an array a of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. 
Return the answer in ascending order. If no such element is found, return list containing [-1]. 
Note: The extra space is only for the array to be returned. Try and perform all operations within the provided array. 

Example 1:
Input:
N = 4
a[] = {0,3,1,2}
Output: 
-1
Explanation: 
There is no repeating element in the array. Therefore output is -1.

Example 2:
Input:
N = 5
a[] = {2,3,1,2,3}
Output: 
2 3 
Explanation: 
2 and 3 occur more than once in the given array.
"""

def duplicates(arr):
    n = len(arr)
    seen = {}
    duplicate = []

    for i in arr:
        if i in seen:
            duplicate.append(i)
        else:
            seen[i] = True

    if not duplicate:
        duplicate.append(-1)

    set_duplicate = set(duplicate)

    return sorted(list(set_duplicate))

arr1 = [2,3,1,2,3]
arr2 = [0,1,4,3]

print(duplicates(arr1))
print(duplicates(arr2))