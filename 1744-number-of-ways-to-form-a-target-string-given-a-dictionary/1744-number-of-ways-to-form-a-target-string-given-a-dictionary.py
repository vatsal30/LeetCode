class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10 ** 9 + 7
        cnt = [[0] * 27 for _ in range(len(words[0]))]
        for word in words:
            for i, c in enumerate(word):
                cnt[i][ord(c) - ord('a')] += 1
        dp = {}
        def checker(i, k):
            if k == len(target):
                return 1
            if i == len(words[0]):
                return 0
            if (i, k) in dp:
                return dp[(i,k)]
            char = target[k]
            dp[(i, k)] = checker(i + 1, k)
            dp[(i, k)] += cnt[i][ord(char) - ord('a')] * checker(i + 1, k + 1)
            return dp[(i, k)] % mod
        
        ans = checker(0, 0)
        return ans