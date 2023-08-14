def print_pascals_triangle(n):
    for line in range(1, n + 1):
        value = 1
        # Print spaces to center the row
        for i in range(n - line):
            print("  ", end="")
        for i in range(1, line + 1):
            print(f"{value:3}", end=" ")
            value = value * (line - i) // i
        print()

# Test the function
num_rows = 6
print_pascals_triangle(num_rows)