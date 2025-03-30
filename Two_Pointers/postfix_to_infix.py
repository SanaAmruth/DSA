def postfix_to_infix(expression):
    # Create a stack to store intermediate results
    stack = []
    
    # Iterate through each character in the expression
    for char in expression:
        # Skip whitespace
        if char.isspace():
            continue
            
        # If character is alphanumeric, push to stack
        if char.isalnum():
            stack.append(char)
        # If character is an operator
        elif char in {'+', '-', '*', '/', '^'}:
            # Pop two operands from stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Create infix expression and push back to stack
            infix_expr = f"({operand1}{char}{operand2})"
            stack.append(infix_expr)
    
    # Final result should be single element in stack
    return stack[0]

# Test cases
test_expressions = [
    "ab+",           # Basic addition
    "ab+c*",         # Multiple operators
    "abc*+",         # Different order
    "234*+",         # With numbers
    "ab+c*d-"        # Complex expression
]

for expr in test_expressions:
    result = postfix_to_infix(expr)
    print(f"Postfix: {expr}")
    print(f"Infix:   {result}\n")