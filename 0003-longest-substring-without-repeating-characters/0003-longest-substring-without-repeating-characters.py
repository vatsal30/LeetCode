class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        visited = {}
        for right in range(len(s)):
            if s[right] in visited and left <= visited[s[right]]:
                left = visited[s[right]] + 1
            visited[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans