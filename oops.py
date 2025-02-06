def is_balanced(input_string):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    
    for char in input_string:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return not stack

# Example usage
user_input = input("Enter a string of brackets: ")
if is_balanced(user_input):
    print("The string has balanced brackets.")
else:
    print("The string does not have balanced brackets.")