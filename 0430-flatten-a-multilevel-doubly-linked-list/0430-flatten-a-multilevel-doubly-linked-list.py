"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curr = head  
        while curr:
            if curr.child:
                flatten = self.flatten(curr.child)
                curr.child = None
                next_p = curr.next
                curr.next = flatten
                flatten.prev = curr
                
                    
                while curr and curr.next:
                    curr = curr.next
                if next_p:
                    curr.next = next_p
                    next_p.prev = curr
            curr = curr.next
        return head
        