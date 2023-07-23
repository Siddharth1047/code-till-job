# Find if a number is Fibonacci or not

import math as m
def perfect_square(n):
    root = int(m.sqrt(n))
    return root * root == n

def fibonacci(num):
    if perfect_square(5 * num * num + 4) or perfect_square(5 * num * num - 4):
        return "yes"
    else:
        return "no"
    
num = 34 # try 8,1,2,21
num1 = 67
print(fibonacci(num))
print(fibonacci(num1))