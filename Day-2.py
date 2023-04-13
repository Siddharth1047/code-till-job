# Kadane's Algorithm

def kadane(arr):
    n = len(arr)
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, n): # start iterating from second element
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

arr1 = [1,2,3,-2,5]
arr2 = [-1,-2,-3,-4]

print("Max subarray is: ", kadane(arr1)) # Output: 9
print("Max subarray is: ", kadane(arr2)) # Output: -1