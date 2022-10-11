class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (len(needle) > len(haystack)):
            return -1
        for i in range(len(haystack)):
            if (haystack[i] == needle[0]):
                j = i + len(needle) - 1
                temp = i + 1
                k = 1
                while (j >= temp and j < len(haystack)):
                    print(haystack[temp], needle[k], haystack[j], needle[-k])
                    if (haystack[temp] == needle[k] and haystack[j] == needle[-k]):
                        temp += 1
                        k += 1
                        j -= 1
                    else:
                        break
                if (j < temp):
                    return i
        return -1