class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True
        
        matched = set()
        rows = len(board)
        columns = len(board[0])
        
        def dfs(r, c, node, path):
            if node.is_end:
                matched.add(path)
                node.is_end = False
            
            if r < 0 or c < 0 or r >= rows or c >= columns:
                return

            ch = board[r][c]
            if ch not in node.children:
                return
            
            board[r][c] = '#'
            child = node.children[ch]
            for dr, dc in [(1, 0), [-1, 0], [0, 1], [0, -1]]:
                dfs(r + dr, c + dc, child, path + ch)
            board[r][c] = ch
    
            if not child.children:
                del node.children[ch]

        for i in range(rows):
            for j in range(columns):
                dfs(i, j, root, "")
        return list(matched)
