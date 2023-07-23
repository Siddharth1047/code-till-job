# For this challenge you will determine the largest double digit number.
# have the function Math(num) take the num parameter being passed and 
# determine the largest double digit number within the whole number. 
# For example: if num is 4759472 then your program should return 94 because 
# that is the largest double digit number. The input will always contain at least two positive digits. 

def Math(num):
    num_str = str(num)
    greatest_digit = -1

    for i in range(len(num_str) - 1):
        two_digit = int(num_str[i:i+2])
        if two_digit > greatest_digit:
            greatest_digit = two_digit

    return greatest_digit

num = 4759472
print(Math(num))
