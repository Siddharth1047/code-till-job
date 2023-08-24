# Recursive 0/1 Knapsack Problem

from functools import wraps

# Memoization
def memoize(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
        
    return wrapper
    
@memoize
def knapSack(W, wt, val, n):
    if W == 0 or n == 0:
        return 0
    
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n - 1)
    else:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1), knapSack(W, wt, val, n - 1))

# Test Cases
W1 = 50
wt1 = [10, 20, 30]
val1 = [60, 100, 120]
n1 = len(wt1)
result1 = knapSack(W1, wt1, val1, n1)
print("Test Case 1 - Expected:", 220, "Actual:", result1)

W2 = 15
wt2 = [2, 3, 4, 5]
val2 = [3, 4, 5, 6]
n2 = len(wt2)
result2 = knapSack(W2, wt2, val2, n2)
print("Test Case 2 - Expected:", 7, "Actual:", result2)

W3 = 7
wt3 = [1, 3, 4, 5]
val3 = [1, 4, 5, 7]
n3 = len(wt3)
result3 = knapSack(W3, wt3, val3, n3)
print("Test Case 3 - Expected:", 9, "Actual:", result3)

W4 = 10
wt4 = [5, 4, 6, 3]
val4 = [10, 40, 30, 50]
n4 = len(wt4)
result4 = knapSack(W4, wt4, val4, n4)
print("Test Case 4 - Expected:", 90, "Actual:", result4)

W5 = 8
wt5 = [2, 2, 3]
val5 = [3, 5, 7]
n5 = len(wt5)
result5 = knapSack(W5, wt5, val5, n5)
print("Test Case 5 - Expected:", 10, "Actual:", result5)

# Sometimes (in case of larger inputs) recursion based solution for 0/1 knapsack rpoblem fails because of redundant calculations.
# Hence, try using DP for solving this problem, it's more efficient and clean.