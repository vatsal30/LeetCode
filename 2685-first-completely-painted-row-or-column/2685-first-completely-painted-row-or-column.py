class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        pos = [None] * (m*n)
        for i in range(m):
            for j in range(n):
                pos[mat[i][j] - 1] = (i, j)
        
        rows = [0] * m
        cols = [0] * n
        for idx, ele in enumerate(arr):
            i, j = pos[ele - 1]
            rows[i] += 1
            cols[j] += 1
            if cols[j] == m:
                return idx
            if rows[i] == n:
                return idx
