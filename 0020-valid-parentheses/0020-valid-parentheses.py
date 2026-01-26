class Solution:
    def isValid(self, s: str) -> bool:
        checker = []
        parenMap = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in parenMap:
                if len(checker) == 0 or checker.pop() != parenMap[c]:
                    return False
            else:
                checker.append(c)
        return len(checker) == 0

        