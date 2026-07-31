class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx):
            if len(word) == idx:
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[idx]:
                return False
            tmp = board[r][c]
            board[r][c] = '#'
            found = any([dfs(r + dr, c + dc, idx + 1) for dr, dc in DIRECTION])
            board[r][c] = tmp
            return found
        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
