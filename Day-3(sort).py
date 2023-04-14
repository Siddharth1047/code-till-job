# Bubble Sort

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubbly = bubble_sort([20,50,30,100,60])
print("Bubble Sorted Array is: ", bubbly)

# Quick Sort

def quick_sort(arr2):

    if len(arr2) <= 1:
        return arr2
    
    pivot = arr2[len(arr2) // 2]
    left = []
    middle = []
    right = []

    for x in arr2:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)

arr2 = [20,30,43,12,100,56,10]
sorted_arr = quick_sort(arr2)
print("Quick Sorted Array is: ", sorted_arr)