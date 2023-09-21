# Find the missing and duplicate value in a sorted array.
# Example:
# Input: [1,2,3,3,5]
# Output: 3,4 (duplicate, missing)

def findDuplicate(arr):
    n = len(arr)
    duplicate = None
    seen = set()

    for i in arr:
        if i in seen:
            duplicate = i
            break
        seen.add(i)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)

    missing_value = expected_sum - actual_sum + duplicate

    return duplicate, missing_value

arr = [1,2,3,4,5,6,6,8,9]
print(findDuplicate(arr))