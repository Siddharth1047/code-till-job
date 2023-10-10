# Find 2nd largest and 2nd smallest element in an array
def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    slargest = s_largest(n,a)
    ssmallest = s_smallest(n,a)
    return slargest, ssmallest

def s_largest(n, a):
    largest = a[0]
    s_largest = -1
    for i in a:
        if i > largest:
            s_largest = largest
            largest = i
        elif i < largest and i > s_largest:
            s_largest = i
    return s_largest

def s_smallest(n, a):
    smallest = a[0]
    s_smallest = float('inf')
    for i in a:
        if i < smallest:
            s_smallest = smallest
            smallest = i
        elif i > smallest and i < s_smallest:
            s_smallest = i
    return s_smallest
    
a = [3,5,4,67,12,32,12,5,56,90,90]
n = len(a)
print(getSecondOrderElements(n, a))