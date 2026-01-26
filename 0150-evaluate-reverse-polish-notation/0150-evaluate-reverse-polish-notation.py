class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        expr = ['+', '-', '*', '/']
        for token in tokens:
            if token in expr:
                val2 = stack.pop()
                val1 = stack.pop()
                result = eval(val1 + token + val2)
                stack.append(str(int(result)))
                
            else:
                stack.append(token)
        return int(stack.pop())

        