# Reverse a String

def reverse(str):
    print(str[::-1])

str = "hii boy"
reverse(str)

# Find factorial of a number

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(4))