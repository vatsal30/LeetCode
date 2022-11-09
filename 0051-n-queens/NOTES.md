​**Solution with higher time complexity:**

```
class Solution:
    def isSafe(self, row, col, board, n):
        duprow = row
        dupcol = col
        
        while(row>=0 and col>=0):
            if (board[row][col] == 'Q'):
                return False
            row -= 1
            col -= 1
        
        col = dupcol
        row = duprow
        while(col>=0):
            if (board[row][col] == 'Q'):
                return False
            col -= 1
        
        col = dupcol
        while(col>=0 and row<n):
            if(board[row][col] == 'Q'):
                return False
            row += 1
            col -= 1
        return True
    def solver(self, col, board, ans, n):
        if (col == n):
            ans.append(board.copy())
            return
        for row in range(n):
            if (self.isSafe(row, col, board, n)):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.solver(col+1, board, ans, n)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ["."*n for i in range(n)]
        self.solver(0, board, ans, n)
        return ans
```
