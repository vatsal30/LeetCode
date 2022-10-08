# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        adder = 0
        ans = l1
        prev = None
        while l1 and l2:
            l1.val = l1.val + l2.val + adder
            adder = 0
            if (l1.val > 9):
                l1.val = l1.val % 10
                adder = 1
            prev = l1
            l1 = l1.next
            l2 = l2.next
        if (l2):
            prev.next = l2
            l1 = l2
        while l1:
            prev = l1
            l1.val = l1.val + adder
            adder = 0
            if (l1.val > 9):
                l1.val = l1.val % 10
                adder = 1
            l1 = l1.next
        if adder:
            prev.next = ListNode(adder)
        return ans