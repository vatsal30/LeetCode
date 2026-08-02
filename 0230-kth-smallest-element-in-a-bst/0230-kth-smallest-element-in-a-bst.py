# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        cnt = 0
        while curr:
            
            if not curr.left:
                cnt +=1
                if cnt == k:
                    return curr.val
                curr = curr.right
                continue
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right
            if not pred.right:
                pred.right = curr
                curr = curr.left
            else:
                pred.right = None
                cnt +=1
                if cnt == k:
                    return curr.val
                curr = curr.right