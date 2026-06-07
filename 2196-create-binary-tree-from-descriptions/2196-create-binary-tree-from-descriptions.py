# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        child_s = set()
        for parent, child, isLeft in descriptions:
            if parent in node_map:
                parent_n = node_map[parent]
            else:
                parent_n = TreeNode(parent)
                node_map[parent] = parent_n
            if child in node_map:
                child_n = node_map[child]
            else:
                child_n = TreeNode(child)
                node_map[child] = child_n
            if isLeft:
                parent_n.left = child_n
            else:
                parent_n.right = child_n
            child_s.add(child)
        return node_map[[key for key in node_map if key not in child_s][0]]
            
