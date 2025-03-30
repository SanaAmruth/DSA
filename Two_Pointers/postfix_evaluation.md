# Postfix Expression Evaluation

## Introduction
Postfix notation (Reverse Polish Notation) is an arithmetic expression format where **operators appear after operands** (e.g., `AB+` instead of `A + B`).

Evaluating a **postfix expression** is efficient because it does not require parentheses or operator precedence rules.

## Algorithm: Postfix Evaluation
We use a **stack** to store operands and compute results as we scan the expression.

### **Steps**
1. **Initialize an empty stack**.
2. **Scan the postfix expression from left to right**:
   - **Operand (A-Z, 0-9)** → Push onto the stack.
   - **Operator (+, -, *, /, ^)** → Pop **two operands**, apply the operator, and push the result back.
3. **Final result** is at the top of the stack.

### **Example**
#### **Input (Postfix Expression)**: `23*5+`
#### **Steps**:
| Symbol | Stack (Top -> Bottom) |
|--------|----------------------|
| `2`    | `2`                  |
| `3`    | `3 2`                |
| `*`    | `6`                  |
| `5`    | `5 6`                |
| `+`    | `11`                 |

#### **Output**: `11`

## Implementation (Python)
```python
from collections import deque

def check_num(i):
    if (i[0] == '-' and i[1:].isdigit() == True) or i.isdigit() == True:
        return True
    return False

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        num = 0
        for i in tokens:
            if check_num(i) == True:
                print(i)
                stack.append(int(i))
                print(stack)
            else:
                print(i)
                if i == '*':
                    two = stack.pop()
                    one = stack.pop()
                    stack.append(one*two)
                elif i == '+':
                    two = stack.pop()
                    one = stack.pop()
                    stack.append(one+two)
                elif i == '-':
                    two = stack.pop()
                    one = stack.pop()
                    stack.append(one-two)
                else:
                    two = stack.pop()
                    one = stack.pop()
                    if one/two<0 and one % two!=0:
                        stack.append(one//two + 1)
                    else:
                        stack.append(one//two)
        return stack[-1]
```

## Summary
- Use a **stack** to store operands.
- Push **operands** directly.
- Pop **two operands** for an **operator**, compute, and push the result back.
- The final value in the stack is the result of the expression.

Check the **Infix to Postfix Conversion** document to learn how to convert expressions before evaluating!

