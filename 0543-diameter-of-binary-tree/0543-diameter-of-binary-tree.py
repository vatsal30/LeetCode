class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = -1
        self.dfs(root)
        return self.maxi

    def dfs(self, root):
        if not root: return 0
        else:
            left = self.dfs(root.left)
            right = self.dfs(root.right)
            self.maxi = max(self.maxi, left+right)
            return 1 + max(left, right)