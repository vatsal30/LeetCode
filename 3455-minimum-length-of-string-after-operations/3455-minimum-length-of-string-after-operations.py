class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        ans = sum(1 if val % 2 == 1 else 2 for val in freq.values())
        return ans