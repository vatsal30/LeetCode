# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        queue = deque([])
        stack = [root]
        while stack:
            node = stack.pop()
            queue.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        queue.popleft()
        curr = root
        while queue:
            curr.left = None
            curr.right = TreeNode(queue.popleft())
            curr = curr.right
