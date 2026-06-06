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
        stack = []
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
            elif not curr.next and stack:
                next_n = stack.pop()
                curr.next = next_n
                next_n.prev = curr
            curr = curr.next
        return head

        return head
        