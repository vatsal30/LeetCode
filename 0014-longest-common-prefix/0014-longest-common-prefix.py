class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # commonPrefix = ""
        i = 0
        while(True):
            if (i >= len(strs[0])):
                return strs[0][:i]
            pattern = strs[0][i]
            for j in range(1, len(strs)):
                if (i < len(strs[j]) and strs[j][i]==pattern):
                    continue
                else:
                    return strs[0][:i]
            # commonPrefix += pattern
            i += 1
        