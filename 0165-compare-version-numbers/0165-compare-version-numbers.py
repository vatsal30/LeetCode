class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        first = 0
        second = 0
        len_v1 = len(version1)
        len_v2 = len(version2)
        n1 = 0
        n2 = 0
        while(first < len_v1 or second < len_v2):
            while(first<len_v1 and version1[first] != '.'):
                n1 = n1*10 + int(version1[first])
                first += 1
            while(second<len_v2 and version2[second] != '.'):
                n2 = n2*10 + int(version2[second])
                second += 1
            if (n1 > n2):
                return 1
            if (n2 > n1):
                return -1
            n1 = 0
            n2 = 0
            second += 1
            first += 1
        return 0