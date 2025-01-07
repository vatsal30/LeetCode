# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        prev = ans
        sum_val = 0
        while l1 is not None or l2 is not None:
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            newNode = ListNode(sum_val % 10)
            prev.next = newNode
            prev = newNode
            sum_val = sum_val // 10
        if sum_val:
            new_node = ListNode(sum_val)
            prev.next = new_node
        return ans.next