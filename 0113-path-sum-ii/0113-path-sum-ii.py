# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def pathSumWithPath(node, target, path):
            path.append(node.val)
            if not node.left and not node.right:
                if node.val == target:
                    ans.append(path.copy())
                path.pop()
                return
            if node.left:
                pathSumWithPath(node.left, target - node.val, path)
            if node.right:
                pathSumWithPath(node.right, target - node.val, path)
            path.pop()
        pathSumWithPath(root, targetSum, [])
        return ans
        