def print_a():
    # Print the top half of the "A"
    for i in range(5):
        for j in range(9):
            if j == 4 - i or j == 4 + i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Print the bottom half of the "A"
    for i in range(3):
        for j in range(9):
            if j == 1 or j == 7:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Call the function to print the "A"
print_a()
