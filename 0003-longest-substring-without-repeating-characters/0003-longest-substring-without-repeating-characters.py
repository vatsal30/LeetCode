class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        seen = {}
        while r < len(s):
            seen[s[r]] = seen.get(s[r], 0) + 1
            if seen[s[r]] > 1:
                while s[l] != s[r]:
                    seen[s[l]] -= 1
                    l += 1
                seen[s[l]] -= 1
                l += 1
                
            max_len = max((r - l + 1), max_len)
            r += 1
        return max_len