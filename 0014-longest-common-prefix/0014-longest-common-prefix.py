class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        i = 0
        while(True):
            print(len(strs[0]))
            if (i >= len(strs[0])):
                return commonPrefix
            pattern = strs[0][i]
            for j in range(1, len(strs)):
                if (i < len(strs[j]) and strs[j][i]==pattern):
                    continue
                else:
                    return commonPrefix
            commonPrefix += pattern
            i += 1
        