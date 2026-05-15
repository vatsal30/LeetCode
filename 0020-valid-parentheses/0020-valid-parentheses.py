class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {'}': '{', ']': '[', ')':'('}
        stack = []
        for paren in s:
            if paren in mapper:
                if stack and stack[-1] == mapper[paren]:
                    stack.pop()
                else:
                    return False          
            else:
                stack.append(paren)
        return not stack
        