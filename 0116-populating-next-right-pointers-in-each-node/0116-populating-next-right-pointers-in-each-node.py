"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        ## Iterative
        leftnode = root
        while leftnode.left:
            curr = leftnode
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            leftnode = leftnode.left
        # Recursive
        # def dfs(node):
        #     if node.left:
        #         node.left.next = node.right
        #         dfs(node.left)
        #     if node.right:
        #         if node.next:
        #             node.right.next = node.next.left
        #         dfs(node.right)
        # dfs(root)
        return root
            
        