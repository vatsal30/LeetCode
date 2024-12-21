class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = 0 
        while idx < len(haystack):
            if haystack[idx] == needle[0] and haystack[idx:idx+len(needle)] == needle:
                return idx
            idx += 1
        return -1