# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        main_prev = dummy
        while True:
            kth_node = self.getKth(main_prev, k)
            if not kth_node:
                break
            main_next = kth_node.next
            
            prev, curr = kth_node.next, main_prev.next
            while curr != main_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            temp = main_prev.next
            main_prev.next = kth_node
            main_prev = temp
        return dummy.next
                