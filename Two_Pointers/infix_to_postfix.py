


def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = []
    for char in expression:
        if char.isalnum():  # If the character is an operand (number or letter)
            postfix.append(char)
        elif char == '(':  # If the character is '(', push it to the stack
            stack.append(char)
        elif char == ')':  # If the character is ')', pop from stack until '('
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Pop the '(' from the stack
        else:  # If the character is an operator
            while (stack and stack[-1] != '(' and
                   precedence[char] <= precedence[stack[-1]]):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:  # Pop all the operators from the stack
        postfix.append(stack.pop())

    return ''.join(postfix)






# Infix to Postfix conversion
expression = "(a+b)"
print(infix_to_postfix(expression))