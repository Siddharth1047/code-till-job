# Find duplicate in an array.

def duplicate(arr,n):
    seen = {}
    duplicates = set()

    for num in arr:
        if num in seen:
            seen[num] += 1
            duplicates.add(num)
        else:
            seen[num] = 1
        
    return duplicates

result = duplicate([1,2,3,5,3,2,7,6,9,1,2,3],12)
print(result)
