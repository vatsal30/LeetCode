from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False
        mapper = {}
        mapper2 = {}
        for i in range(len(pattern)):
            if pattern[i] in mapper and mapper[pattern[i]] != s_list[i]:
                return False
            
            if s_list[i] in mapper2 and mapper2[s_list[i]] != pattern[i]:
                return False
            mapper[pattern[i]] = s_list[i]
            mapper2[s_list[i]] = pattern[i]
        return True