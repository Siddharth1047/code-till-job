# Reverse a string

String_me = "I am sexy"
print(String_me[::-1])

# Reverse a list

my_list = [1,2,3,4,5,6]
my_list.reverse()
print(my_list)

# Reverse an integer 

num = 123456
num_str = str(num)
reversed_num = int(num_str[::-1])
print(reversed_num)

# What if number is negative??

def reversed(number):
    reversee = 0
    is_negative = False

    if number < 0:
        is_negative = True
        number = abs(number)

    while number > 0:
        digit = number % 10
        reversee = (reversee * 10) + digit
        number //= 10

    return -reversee if is_negative else reversee

number = 45546776
reversed_number = reversed(number)
print(reversed_number)