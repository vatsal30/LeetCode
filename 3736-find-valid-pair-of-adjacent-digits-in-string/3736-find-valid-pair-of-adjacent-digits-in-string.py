class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter()
        for char in s:
            count[char] += 1
        for idx in range(1, len(s)):
            if count[s[idx]] == int(s[idx]) and count[s[idx-1]] == int(s[idx-1]) and (s[idx] != s[idx-1]):
                return s[idx-1: idx+1]
        return ""
            
        