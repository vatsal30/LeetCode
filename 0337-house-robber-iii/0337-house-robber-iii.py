# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if node == None:
            return [0, 0]
        left_m = self.dfs(node.left)
        right_m = self.dfs(node.right)

        with_r = left_m[1] + right_m[1] + node.val
        without_r = max(left_m) + max(right_m)
        return [with_r, without_r]
        
    def rob(self, root: Optional[TreeNode]) -> int:
        money = self.dfs(root)
        return max(money)
