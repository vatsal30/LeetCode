from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False
        mapper = {}
        mapper2 = {}
        for i in range(len(pattern)):
            if pattern[i] not in mapper:
                mapper[pattern[i]] = s_list[i]
            elif mapper[pattern[i]] != s_list[i]:
                return False
            
            if s_list[i] not in mapper2:
                mapper2[s_list[i]] = pattern[i]
            elif mapper2[s_list[i]] != pattern[i]:
                return False
        return True