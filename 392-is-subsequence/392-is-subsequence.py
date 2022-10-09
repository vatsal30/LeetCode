class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp = 0
        if (len(s) == 0):
            return True
        for i in range(len(t)):
            if (t[i] == s[temp]):
                temp += 1
                if (temp == len(s)):
                    return True
        return False