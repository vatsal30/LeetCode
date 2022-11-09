class Solution:
    def solver(self, col, board, n, leftRow, lowerDiagonal, upperDiagonal):
        if (col == n):
            return 1
        ans = 0
        for row in range(n):
            if (leftRow[row]==0 and lowerDiagonal[row+col] == 0 and upperDiagonal[n - 1 - row + col] == 0):
                leftRow[row] = 1
                lowerDiagonal[row+col] = 1
                upperDiagonal[n - 1 - row + col] = 1
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                ans += self.solver(col+1, board, n, leftRow, lowerDiagonal, upperDiagonal)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
                leftRow[row] = 0
                lowerDiagonal[row+col] = 0
                upperDiagonal[n - 1 - row + col] = 0
        return ans
            
        
    def totalNQueens(self, n: int) -> int:   
        board = ["."*n for i in range(n)]
        leftRow = [0 for i in range(n)]
        lowerDiagonal = [0 for i in range(2*n-1)]
        upperDiagonal = [0 for i in range(2*n-1)]
        ans = self.solver(0, board, n, leftRow, lowerDiagonal, upperDiagonal)
        return ans
    
        