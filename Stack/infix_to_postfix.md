# Infix to Postfix Expression Conversion

## Introduction
Infix notation is the standard arithmetic notation where operators are placed between operands (e.g., `A + B`). However, for easier computation, it is often converted to **Postfix notation** (Reverse Polish Notation), where operators come **after** operands (e.g., `AB+`).

## Operator Precedence and Associativity
To correctly convert an infix expression to postfix, we need to consider **operator precedence** and **associativity**:

| Operator | Precedence | Associativity |
|----------|-----------|--------------|
| `^`      | 3         | Right-to-left |
| `* /`    | 2         | Left-to-right |
| `+ -`    | 1         | Left-to-right |
| `(` `)`  | -         | N/A |

## Algorithm: Infix to Postfix Conversion
We use a **stack** to handle operators while scanning the infix expression.

### **Steps**
1. **Initialize an empty stack** for operators and an empty list for output.
2. **Scan the expression from left to right**:
   - **Operand (A-Z, 0-9)** → Add to output.
   - **Operator (+, -, *, /, ^)** → Pop higher/equal precedence operators from the stack to output, then push the current operator.
   - **Left Parenthesis (`(`)** → Push onto the stack.
   - **Right Parenthesis (`)`)** → Pop from the stack to output until a left parenthesis is found.
3. **Pop remaining operators** from the stack and append to output.

### **Example**
#### **Input (Infix)**: `A + B * C`
#### **Steps**:
| Symbol | Stack   | Output  |
|--------|--------|--------|
| `A`    |        | `A`    |
| `+`    | `+`    | `A`    |
| `B`    | `+`    | `A B`  |
| `*`    | `+ *`  | `A B`  |
| `C`    | `+ *`  | `A B C`|
| End    |        | `A B C * +` |

#### **Output (Postfix)**: `A B C * +`

## Implementation (Python)
```python
from collections import deque

def precedence(op):
    if op in {'+', '-'}:
        return 1
    if op in {'*', '/'}:
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = deque()
    output = []
    for char in expression:
        if char.isalnum():  # Operand
            output.append(char)
        elif char == '(':  # Left parenthesis
            stack.append(char)
        elif char == ')':  # Right parenthesis
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:  # Operator
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return ''.join(output)

expr = "A+B*C"
print(infix_to_postfix(expr))  # Output: ABC*+
```

## Summary
- Use a **stack** to handle operators and precedence.
- Append **operands directly** to output.
- **Pop operators based on precedence** before pushing a new operator.
- Handle **parentheses separately**.

Check the **Postfix Evaluation** document to learn how to evaluate postfix expressions!

