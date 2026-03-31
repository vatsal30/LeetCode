import math 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                y = stack.pop()
                x = stack.pop()
                result = x + y
                stack.append(result)
            elif token == '-':
                y = stack.pop()
                x = stack.pop()
                result = x - y
                stack.append(result)
            elif token == '*':
                y = stack.pop()
                x = stack.pop()
                result = x * y
                stack.append(result)
            elif token == '/':
                y = stack.pop()
                x = stack.pop()
                result = math.trunc(x / y)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]
