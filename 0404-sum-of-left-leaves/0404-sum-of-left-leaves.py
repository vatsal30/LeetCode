# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0;
        queue = []
        queue.append((root, False))
        while queue:
            
            for i in range(len(queue)):
                node,isLeft = queue.pop()
                isLeaf = True
                if node.left:
                    queue.append((node.left, True))
                    isLeaf = False
                if node.right:
                    queue.append((node.right, False)) 
                    isLeaf = False
                if isLeaf and isLeft:
                     ans += node.val
        return ans
            
                