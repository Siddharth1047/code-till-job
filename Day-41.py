# Find peak element in a array 
# Peak element is the greatest element in it's neighbourhood
# Example: - arr == [1,2,3] Peak element is 3(i.e. = 2)
# 2 is it's position in ana array 

def Mid(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left