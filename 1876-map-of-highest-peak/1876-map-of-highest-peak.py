class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ans = []
        m = len(isWater)
        n = len(isWater[0])

        for i in range(m):
            temp = []
            for j in range(n):
                if isWater[i][j]:
                    temp.append(0)
                    queue.append((i, j))
                else:
                    temp.append(-1)
            ans.append(temp)
        
        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if x >= 0 and y >= 0 and x < m and y < n and ans[x][y] == -1:
                    ans[x][y] = ans[i][j] + 1
                    queue.append((x, y))
        return ans
        


        