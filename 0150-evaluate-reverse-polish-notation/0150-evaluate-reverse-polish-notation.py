class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        expr = ['+', '-', '*', '/']
        for token in tokens:
            if token == "+":
                val2 = stack.pop()
                val1 = stack.pop()
                result = val1 + val2
                stack.append(result)
            elif token == "-":
                val2 = stack.pop()
                val1 = stack.pop()
                result = val1 - val2
                stack.append(result)
            elif token == "*":
                val2 = stack.pop()
                val1 = stack.pop()
                result = val1 * val2
                stack.append(result)
            elif token == "/":
                val2 = stack.pop()
                val1 = stack.pop()
                result = float(val1) / val2
                stack.append(int(result))
            else:
                stack.append(int(token))
        return stack.pop()

        