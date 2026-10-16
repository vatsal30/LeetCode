class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []
        freq_s = [0] * 26
        freq_p = [0] * 26
        ans = []

        for i in range(len(p)):
            freq_s[ord(s[i]) - 97] += 1
            freq_p[ord(p[i]) - 97] += 1

        left = 0
        if freq_s == freq_p:
            ans.append(left)

        for right in range(len(p), len(s)):
            freq_s[ord(s[left]) - 97] -= 1
            freq_s[ord(s[right]) - 97] += 1
            left += 1

            if freq_s == freq_p:
                ans.append(left)
            
        return ans
        