class Solution:
    def isPalindrom(self, s: str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        result, perm = [], []
        def backtrack(start):
            if len(s) == start:
                result.append(perm[:])
            for i in range(start, len(s)):
                if self.isPalindrom(s[start:i+1]):
                    perm.append(s[start:i+1])
                    backtrack(i + 1)
                    perm.pop()
        backtrack(0)
        return result