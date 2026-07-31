class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = cols = n
        cols = set()
        diag = set()
        anti_diag = set()
        result, queen = [], []
        
        board = [["."] * n for _ in range(n)]
        def backtrack(start):
            if start == n:
                result.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                diag_id = start - c
                anti_diag_id = start + c
                if c in cols or diag_id in diag or anti_diag_id in anti_diag:
                    continue

                cols.add(c)
                diag.add(diag_id)
                anti_diag.add(anti_diag_id)
                board[start][c] = 'Q'

                backtrack(start + 1)

                board[start][c] = '.'
                cols.remove(c)
                diag.remove(diag_id)
                anti_diag.remove(anti_diag_id)
        backtrack(0)
        return result

        
        