class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # In terms of memory it doesn't matter it is takes up same amount of space and time almost
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows): 
            temp = [1] * (i + 1)
            for j in range(1, i // 2 + 1):
                temp[j] = ans[-1][j] + ans[-1][j-1]
                temp[i - j] = temp[j]
            ans.append(temp)
        return ans
        
        # In Efficient Solution In terms of spce
        # For n = 5 we are creating an array like this
        # [1, 1, 1 , 1 , 1]
        # [1, 2, 3 , 4 , 5]
        # [1, 3, 6 , 10, 15]
        # [1, 4, 10, 20, 35]
        # [1, 5, 15, 35, 70]
        # Now rotate it by 45 degree and you get the results

        # dp = [[1] * numRows for _ in range(numRows)]
        # for i in range(1, numRows):
        #     for j in range(1, numRows - i):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # ans = []
        # for i in range(numRows):
        #     temp = []
        #     k = i
        #     for j in range(0, i + 1):
        #         temp.append(dp[k][j])
        #         k -= 1
        #     ans.append(temp)
        # return ans