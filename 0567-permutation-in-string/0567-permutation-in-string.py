class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_map = [0] * 26
        s2_map = [0] * 26

        for i in range(len(s1)):
            s1_map[ord(s1[i]) - 97] += 1
            s2_map[ord(s2[i]) - 97] += 1
        
        matches = 0
        for i in range(26):
            if s1_map[i] == s2_map[i]:
                matches += 1
        
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            ridx = ord(s2[right]) - 97
            s2_map[ridx] += 1
            if (s2_map[ridx] == s1_map[ridx]):
                matches += 1
            elif s2_map[ridx] == s1_map[ridx] + 1:
                matches -= 1
            lidx = ord(s2[right - len(s1)]) - 97
            s2_map[lidx] -= 1
            if s2_map[lidx] == s1_map[lidx]:
                matches += 1
            elif s2_map[lidx] == s1_map[lidx] - 1:
                matches -= 1
            
        return matches == 26