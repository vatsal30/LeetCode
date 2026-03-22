from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_c = [0] * 26
        s2_c = [0] * 26

        for i in range(len(s1)):
            s1_c[ord(s1[i]) - 97] += 1
            s2_c[ord(s2[i]) - 97] += 1
        
        if s1_c == s2_c:
            return True

        left = 1
        for right in range(len(s1), len(s2)):
            s2_c[ord(s2[left - 1]) - 97] -= 1
            s2_c[ord(s2[right]) - 97] += 1

            if s1_c == s2_c:
                return True

            left += 1
        return False