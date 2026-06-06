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
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        while curr:
            dummy = Node()
            tail = dummy
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            curr = dummy.next
        return root
        # Initial solution scan forward approach
        # leftmost = root
        # while leftmost:
        #     curr = leftmost
        #     leftmost = None
        #     while curr:
        #         next_n = curr.next
        #         if curr.left:    
        #             if not leftmost:
        #                 leftmost = curr.left
        #             if curr.right:
        #                 curr.left.next = curr.right
        #             else:
        #                 while next_n:
        #                     if next_n.left:
        #                         curr.left.next = next_n.left
        #                         break
        #                     elif next_n.right:
        #                         curr.left.next = next_n.right
        #                         break
        #                     else:
        #                         next_n = next_n.next
        #         if curr.right:
        #             if not leftmost:
        #                 leftmost = curr.right
        #             while next_n:
        #                 if next_n.left:
        #                     curr.right.next = next_n.left
        #                     break
        #                 elif next_n.right:
        #                     curr.right.next = next_n.right
        #                     break
        #                 else:
        #                     next_n = next_n.next
        #         curr = next_n
        # return root
            

        