# https://neetcode.io/problems/evaluate-reverse-polish-notation
# https://www.geeksforgeeks.org/batch/dsa-4/track/DSASP-Stack/video/MTUyMg%3D%3D

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