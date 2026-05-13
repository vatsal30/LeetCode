class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        ans = 0
        visited = {}
        for right in range(len(s)):
            if s[right] in visited and left <= visited[s[right]]:
                ans = max(right - left, ans)
                left = visited[s[right]] + 1
                del visited[s[right]]
            visited[s[right]] = right
        return max(ans, right - left + 1)