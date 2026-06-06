# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def pathSumWithPath(node, target, path):
            if not node:
                return
            path.append(node.val)
            remaining = target - node.val
            if not node.left and not node.right and remaining == 0:
                ans.append(path.copy())
            else:
                pathSumWithPath(node.left, remaining, path)
                pathSumWithPath(node.right, remaining, path)
            path.pop()
        pathSumWithPath(root, targetSum, [])
        return ans
        