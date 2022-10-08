class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                left = max(d[s[i]], left)
            ans = max(ans, i - left + 1)
            d[s[i]] = i+1
        return ans