from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        ans = 0
        checker = defaultdict(int)
        for right in range(len(s)):
            checker[s[right]] = checker[s[right]] + 1
            while checker[s[right]] > 1:
                checker[s[left]] -= 1
                if checker[s[left]] == 0:
                    del checker[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans