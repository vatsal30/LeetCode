from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        s_freq = Counter(s)
        for char in t:
            if char in s_freq and s_freq[char] > 0:
                s_freq[char] -= 1
            else:
                return False
        return True