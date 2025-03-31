# https://neetcode.io/problems/minimum-stack

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val, val])
        else:
            self.stack.append([val,min(self.stack[-1][1], val)])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        # if len(stack) == 0
        return self.stack[-1][1]
