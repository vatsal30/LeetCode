# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # going to middle point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse
        prev, curr = None, slow.next
        while curr is not None:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp

        slow.next = None
        first, second = head, prev
        while first and second:
            if (first.val == second.val):
                first = first.next
                second = second.next
            else:
                return False
        return True