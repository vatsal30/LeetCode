# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev, curr = head, head.next
        while curr and curr.next:
            odd = curr.next
            even = odd.next
            odd.next = prev.next
            prev.next = odd
            curr.next = even
            prev = prev.next
            curr = curr.next

        return head
        