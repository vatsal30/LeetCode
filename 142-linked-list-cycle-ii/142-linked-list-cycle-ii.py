# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow=head
        fast=head
        meetingNode = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                meetingNode = slow
                break
        if meetingNode is None:
            return None
        while head and slow:
            if slow == head:
                return head
            slow = slow.next
            head = head.next
        return None