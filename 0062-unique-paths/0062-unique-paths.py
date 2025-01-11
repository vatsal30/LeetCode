class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * n
        for i in range(m):
            temp = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    temp[j] = 1
                    continue
                up = 0
                if i > 0:
                    up = prev[j]
                left = 0
                if j > 0:
                    left = temp[j-1]
                temp[j] = up + left
            prev = temp
        return prev[n-1]