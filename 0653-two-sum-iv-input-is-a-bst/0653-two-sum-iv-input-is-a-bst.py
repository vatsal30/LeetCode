# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            val = node.val
            if (k - val) in visited:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            visited.add(val)
        return False