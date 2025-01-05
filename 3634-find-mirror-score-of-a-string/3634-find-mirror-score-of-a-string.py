class Solution:
    def calculateScore(self, s: str) -> int:
        alpha = [deque() for _ in range(26)]
        ans = 0
        for idx, c in enumerate(s):
            order = ord(c) - 97
            reverse = abs(order - 25)
            if len(alpha[reverse]) > 0:
                ans += idx - alpha[reverse].pop()
            else:
                alpha[order].append(idx)
        return ans