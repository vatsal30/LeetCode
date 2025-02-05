class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        notEqCount = 0
        firstIdx = 0
        secondIdx = 0
        
        for idx in range(len(s1)):
            if s1[idx] != s2[idx]:
                notEqCount += 1
                if notEqCount > 2:
                    return False
                elif notEqCount == 1:
                    firstIdx = idx
                else:
                    secondIdx = idx
        return s1[firstIdx] == s2[secondIdx] and s1[secondIdx] == s2[firstIdx]