class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)] 
        grids = [[set() for  _ in range(3)] for _ in range(3)]
        for i in range(9):
            rows = set()
            for j in range(9):
                num = board[i][j]
                if board[i][j] == '.':
                    continue
                grid = grids[i//3][j//3]
                if num in rows or num in cols[j] or num in grid:
                    return False
                cols[j].add(num)
                rows.add(num)
                grid.add(num)
        return True

        