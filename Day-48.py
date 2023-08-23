# Boyer-Moore Majority Voting Algorithm
# Used to find the element with highest frequency in an array
# element occuring more than n/2 times is the result (where n = len(arr))

def boyer_moore(arr):
    n = len(arr)
    count = {}

    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for j in count:
        if count[j] > n/2:
            return j
        
arr = [1,1,3,4,6,1,4,1,6,1,1,1,1]
ans = boyer_moore(arr)
print("The majority element is:", ans)

# Another method

def findMajority(arr,n):
    candidate = -1
    vote = 0

    for i in range(n):
        if vote == 0:
            candidate = arr[i]
            vote = 1
        else:
            if arr[i] == candidate:
                vote += 1
            else:
                vote -= 1

    count = 0

    for i in range(n):
        if arr[i] == candidate:
            count += 1

    if count > n // 2:
        return candidate
    else:
        return -1
    
n = len(arr)
majority = findMajority(arr,n)
print("Majority element without dictionary is:", majority)