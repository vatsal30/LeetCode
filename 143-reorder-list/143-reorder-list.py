# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find Middle of the List
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse the second half of the list
        prev, cur = None, slow.next
        while cur:
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after
        slow.next = None
 
        # Merge first and second half of the list
        first_part, second_part = head, prev
        while second_part:
            temp_1, temp_2 = first_part.next, second_part.next
            first_part.next = second_part
            second_part.next = temp_1
            first_part = temp_1
            second_part = temp_2
        