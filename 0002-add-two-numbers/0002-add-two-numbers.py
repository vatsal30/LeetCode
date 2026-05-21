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
            ans = carry
            if l1:
                ans += l1.val
                l1 = l1.next
            if l2:
                ans += l2.val
                l2 = l2.next
            
            digit = ans % 10
            carry = ans // 10
            curr.next = ListNode(digit, None)
            curr = curr.next
        if carry:
            curr.next = ListNode(carry, None)
        return dummy.next
        