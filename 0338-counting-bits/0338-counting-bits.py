class Solution:
    def countBitsWithoutBit(self, n: int) -> List[int]:
        ## DP Solution without bit maniplation
        ans = [0]
        for i in range(1, n + 1):
            ans.append(i % 2 + ans[i // 2])
        return ans

    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = (i & 1) + dp[i >> 1]
        return dp