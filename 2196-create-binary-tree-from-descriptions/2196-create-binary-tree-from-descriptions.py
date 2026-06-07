# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        childrens = set()
        for parent, child, isLeft in descriptions:
            p = node_map.setdefault(parent, TreeNode(parent))
            c = node_map.setdefault(child, TreeNode(child))
            if isLeft:
                p.left = c
            else:
                p.right = c
            childrens.add(child)
        return node_map[(node_map.keys() - childrens).pop()]
            
