# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.inorderList = []
        self.inorder(root)
        node1, node2 = self.findDiscrepancy()
        if node1 and node2:
            print(node1.val)
            print(node2.val)
            node1.val, node2.val = node2.val, node1.val

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.inorderList.append(root)
            self.inorder(root.right)

    def findDiscrepancy(self):
        maxNode = None
        minNode = None

        for i in range(len(self.inorderList)-1):
            if self.inorderList[i].val > self.inorderList[i+1].val:
                maxNode = self.inorderList[i]
                break
        
        for i in range(len(self.inorderList)-1, 0, -1):
            if self.inorderList[i].val < self.inorderList[i-1].val:
                minNode = self.inorderList[i]
                break
        
        return maxNode, minNode