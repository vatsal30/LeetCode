# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, level: int, node_left: Optional[TreeNode], node_right: Optional[TreeNode]):
        if not node_left or not node_right:
            return
        if level % 2 == 0:
            left_val = node_left.val
            node_left.val = node_right.val
            node_right.val = left_val
        self.solve(level+1, node_left.left, node_right.right)
        self.solve(level+1, node_left.right, node_right.left)

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.solve(0, root.left, root.right)
        return root
        