class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in direction:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and mat[i][j] == -1:
                    mat[i][j] = mat[x][y] + 1
                    queue.append((i, j))
        return mat
