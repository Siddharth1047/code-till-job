# Parenthesis Checker

def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else None
            if mapping[char] != top_element:
                return False
        elif char in mapping.values():
            stack.append(char)

    return not stack


# Test example
input_str = "{[()]}"

if is_valid_parentheses(input_str):
    print("The parentheses in the input string are balanced.")
else:
    print("The parentheses in the input string are not balanced.")