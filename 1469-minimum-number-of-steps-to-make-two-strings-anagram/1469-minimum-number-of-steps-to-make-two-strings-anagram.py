class Solution:
    def minSteps(self, s: str, t: str) -> int:
        orig = [0] * 26
        for c in s:
            orig[ord(c) - 97] += 1
        ans = len(s)
        for c in t:
            if orig[ord(c) - 97] > 0:
                orig[ord(c) - 97] -= 1
                ans -= 1
        return ans
        