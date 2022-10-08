class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        left = len(s) - 1
        right = left
        ans = ""
        while (left >= 0):
            if (s[left] == ' '):
                if (s[right] != ' '):
                    ans += s[left+1:right+1] + " "
                right = left - 1
            left -= 1
        ans += s[left+1:right+1]
        return ans