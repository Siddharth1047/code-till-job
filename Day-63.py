"""
CodeForces Beautiful Year
Code - 271A
Link - https://codeforces.com/problemset/problem/271/A
"""
# Initial Solution (Not Accepted)
def hasDistinct(year):
    year_str = str(year)
    year_set = set()
    
    for i in year_str:
        if i in year_set:
            return False
        year_set.add(i)  
    return True
    
y = int(input())    
y += 1
 
while True:
    if hasDistinct(y):
        print(y)
    y += 1

# Optimized Solution (Accepted)
def hasDistinct(year):
    year_str = str(year)
    return len(year_str) == len(set(year_str))
 
y = int(input())
 
while True:
    y += 1
    if hasDistinct(y):
        print(y)
        break