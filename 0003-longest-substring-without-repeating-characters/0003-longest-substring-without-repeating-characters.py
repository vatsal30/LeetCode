class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        seen = {}
        while r < len(s):
            if seen.get(s[r], -1) >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            max_len = max((r - l + 1), max_len)
            r += 1
        return max_len