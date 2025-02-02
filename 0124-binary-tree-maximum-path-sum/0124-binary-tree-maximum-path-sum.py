# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def dfs(node):
            if not node:
                return 0
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)
            nonlocal max_sum
            curr_sum = node.val + left_sum + right_sum
            max_sum = max(max_sum, curr_sum)
            return node.val + max(left_sum, right_sum)
        dfs(root)
        return max_sum