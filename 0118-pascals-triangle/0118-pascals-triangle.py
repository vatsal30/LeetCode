class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] * numRows for _ in range(numRows)]
        for i in range(1, numRows):
            for j in range(1, numRows - i):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        ans = []
        for i in range(numRows):
            temp = []
            k = i
            for j in range(0, i + 1):
                temp.append(dp[k][j])
                k -= 1
            ans.append(temp)
        return ans