class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b_map = {')': '(', '}': '{', ']': '['}
        for b in s:
            if b in '({[':
                stack.append(b)
            elif stack and stack[-1] == b_map[b]:
                stack.pop()
            else:
                return False
        return False if stack else True