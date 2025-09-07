from typing import List
class Solution:          
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left + right)
            elif token == '-':
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left - right)
            elif token == '*':
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left * right)
            elif token == '/':
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left // right)
                if (stack[-1] < 0 and left % right != 0):
                    stack[-1] += 1
            else:
                stack.append(token)
        return int(stack[-1])
print(Solution().evalRPN(["4","-2","/","2","-3","-","-"]))