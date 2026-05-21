"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head
        while curr:
            clone = Node(curr.val, curr.next, None)
            curr.next = clone
            curr = clone.next
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        old = head
        new = head.next
        curr = new
        while curr.next:
            old.next = curr.next
            old = old.next
            if curr.next:
                curr.next = curr.next.next
                curr = curr.next
        return new