# Given an array, find the element which occurs for 'k' times in that array
# Example: - Array = [1,2,3,1,4,4,5,6], k = 2
# Output:- [1,4] (because 1&4 occur 2 times in array)

def function(arr,k):
    count = {}

    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    arr2 = []

    for j in count:
        if count[j] == k:
            arr2.append(j)

    return arr2

arr = [1,2,3,1,4,4,5,6]
k = 2
print(function(arr,k))