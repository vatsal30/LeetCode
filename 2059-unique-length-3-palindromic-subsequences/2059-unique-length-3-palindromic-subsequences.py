class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26
        for idx, c in enumerate(s):
            curr = ord(c) - 97
            if first[curr] == -1:
                first[curr] = idx
            last[curr] = idx
        ans = 0
        for i in range(26):
            if first[i] == -1:
                continue
            uniq = set()
            for j in range(first[i] + 1, last[i]):
                uniq.add(s[j])
            ans += len(uniq)
        return ans