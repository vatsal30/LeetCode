class Solution:
    def isValid(self, row, col, char, board):
        for i in range(len(board)):
            if (board[row][i] == str(char)):
                return False
            if (board[i][col] == str(char)):
                return False
            if (board[3*(row//3) + i//3][3*(col//3) + i%3] == str(char)):
                return False
        return True

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == "."):
                    for char in range(1,10):
                        if (self.isValid(i, j, char, board)):
                            board[i][j] = str(char)
                            if (self.solve(board)):
                                return True
                            else:
                                board[i][j] = "."
                    return False
                            
        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)