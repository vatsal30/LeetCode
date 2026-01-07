class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0 for _ in range(9)] for _ in range(9)]
        cols = [[0 for _ in range(9)] for _ in range(9)]
        boxs = [[0 for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit != ".":
                    digit = int(digit) - 1
                    if rows[i][digit] == 0 and cols[j][digit] == 0 and boxs[i//3+(j//3)*3][digit] == 0:
                        rows[i][digit] = 1
                        cols[j][digit] = 1
                        boxs[i//3 + (j//3)*3][digit]= 1
                    else:
                        print(digit)
                        print(i, j, boxs)
                        return False
        return True
                        