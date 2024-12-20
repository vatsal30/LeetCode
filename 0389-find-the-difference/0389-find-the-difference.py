from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1
        for c in t:
            if s_dict[c] == 0:
                return c
            s_dict[c] -= 1