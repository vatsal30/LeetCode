class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMap = {}
        revMap = {}
        for i in range(len(s)):
            if (charMap.get(s[i]) == None and revMap.get(t[i]) == None):
                charMap[s[i]] = t[i]
                revMap[t[i]] = s[i]
            elif (charMap.get(s[i]) != t[i]):
                return False
        return True