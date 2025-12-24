from stack import Stack

def check_brackets(expression):
    stack = Stack()
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in matching_brackets.values():
            stack.push(char)
        elif char in matching_brackets.keys():
            if stack.is_empty() or stack.peek() != matching_brackets[char]:
                return False
            stack.pop()

    return stack.is_empty()

# Example usage
expressions = ["(1 + 2) * [3 + {4 - 5}]", "((1 + 2) * [3 + {4 - 5}])", "((1 + 2) * [3 + {4 - 5])"]

for expression in expressions:
    result = check_brackets(expression)
    print(f"Expression: {expression} is balanced: {result}")