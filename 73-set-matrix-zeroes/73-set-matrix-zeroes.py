class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        
        r_length = len(matrix)
        c_length = len(matrix[0])
        col0 = 1
        
        for i in range(r_length):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, c_length):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(r_length-1, -1, -1):
            for j in range(c_length-1, 0 , -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
        return matrix