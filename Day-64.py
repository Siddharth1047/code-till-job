"""
CodeForces Insomnia Cure
Code - 148A
Link - https://codeforces.com/problemset/problem/148/A
"""
# accepted code
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
 
count = sum(
    1
    for i in range(1, d + 1)
    if i%k != 0 and i%l != 0 and i%m != 0 and i%n != 0
)
 
print(d - count)

"""
CodeForces Little Elephant and Bits
Code - 258A
Link - https://codeforces.com/problemset/problem/258/A
"""
# Accepted solution
t = int(input())
 
binary_str = str(t)
first_zero_index = binary_str.find('0')
 
if first_zero_index != -1:
    max_binary_str = binary_str[:first_zero_index] + binary_str[first_zero_index + 1:]
else:
    max_binary_str = binary_str[:-1]
print(max_binary_str)