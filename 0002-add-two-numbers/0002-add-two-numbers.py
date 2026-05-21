# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0, None)
        curr = dummy
        while l1 or l2:
            first_val = l1.val if l1 else 0
            second_val = l2.val if l2 else 0
            sum_ans = first_val + second_val + carry
            quo = sum_ans % 10
            carry = sum_ans // 10
            curr.next = ListNode(quo, None)
            curr = curr.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry:
            curr.next = ListNode(1, None)
        return dummy.next
        