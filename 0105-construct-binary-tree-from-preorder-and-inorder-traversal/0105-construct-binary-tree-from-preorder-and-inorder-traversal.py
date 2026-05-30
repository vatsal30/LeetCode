# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {node:i for i, node in enumerate(inorder)}
        pre_idx = 0
        def builder(min_idx, max_idx):
            nonlocal pre_idx
            if pre_idx >= len(preorder):
                return None
            
            node = preorder[pre_idx]
            pre_idx += 1
            in_idx = in_map[node]
            root = TreeNode(node)
            if in_idx > min_idx:
                root.left = builder(min_idx, in_idx - 1)
            if in_idx < max_idx:
                root.right = builder(in_idx + 1, max_idx)
            
            return root
        return builder(0, len(preorder) - 1)