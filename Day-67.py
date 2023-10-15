# Rotate the array to the left by 'k' steps

def rotateArrays(arr, d):
    n = len(arr)
    d = d % n

    arr[:d] = arr[:d][::-1]
    arr[d:] = arr[d:][::-1]
    arr = arr[::-1]
    return arr

arr = [1,2,3,4,5,6]
d = 3
print(rotateArrays(arr,d))