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
        while l1 and l2:
            result = l1.val + l2.val + carry
            top = result % 10
            carry = result // 10
            curr.next = ListNode(top, None)
            curr = curr.next
            print(result)
            l1 = l1.next
            l2 = l2.next
        while l1:
            result = l1.val + carry 
            top = result % 10
            carry = result // 10
            curr.next = ListNode(top, None)
            curr = curr.next
            l1 = l1.next
            
        
        while l2:
            result = l2.val + carry 
            top = result % 10
            carry = result // 10
            curr.next = ListNode(top, None)
            curr = curr.next
            l2 = l2.next
        if carry:
            curr.next = ListNode(1, None)
        return dummy.next
        