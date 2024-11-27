class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        store = []
        expr = ['+', '-', '*', '/']
        for token in tokens:
            if token in expr:
                op2 = store.pop(-1)
                op1 = store.pop(-1)
                match token:
                    case '+':
                        result = int(op1) + int(op2)
                    case '-':
                        result = int(op1) - int(op2)
                    case '*':
                        result = int(op1) * int(op2)
                    case '/':
                        result = int(op1) / int(op2)
                store.append(result)
            else:
                store.append(token)
        return int(store[-1])
        