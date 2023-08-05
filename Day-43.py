# Find average of numbers (take input from user)

def average(size):
    arr = []

    for i in range(0, size):
        element = int(input("Enter the " + str(i) + " positioned integer: "))
        arr.append(element)

    average_num = sum(arr) / len(arr)
    return average_num

size = int(input("Enter the number of integers you want average of: "))
print(average(size))

# Print the highest frequency character in a string

string = input("Enter the character you want: ")

def highest_freq(string):
    char_dict = {}

    for i in string:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1

    max_freq = max(char_dict.values())

    for j in char_dict:
        if char_dict[j] == max_freq:
            print(f"The character '{j}' has the highest frequency, it appears for {max_freq} times")

highest_freq(string)