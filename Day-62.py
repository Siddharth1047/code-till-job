"""
CodeForces Young Physicist.
Code - 69A
Link - https://codeforces.com/problemset/problem/69/A
"""
# Accepted Solution
t = int(input())
a,b,c = 0,0,0

for i in range(t):
    x,y,z = map(int, input().split())
    a += x
    b += y
    c += z

if (a==b==c==0):
    print("YES")
else:
    print("NO")

