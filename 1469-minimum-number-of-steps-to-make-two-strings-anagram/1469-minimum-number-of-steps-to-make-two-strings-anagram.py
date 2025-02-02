class Solution:
    def minSteps(self, s: str, t: str) -> int:
        orig = Counter(s)
        ans = len(s)
        for c in t:
            if orig[c] > 0:
                orig[c] -= 1
                ans -= 1
        return ans
        