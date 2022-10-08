class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', '}':'{', ']': '['}
        stk = []
        for i in s:
            if i not in d:
                stk.append(i)
            else:
                if (len(stk) <=0 or stk.pop() != d[i]):
                    return False
        if len(stk) > 0:
            return False
        return True