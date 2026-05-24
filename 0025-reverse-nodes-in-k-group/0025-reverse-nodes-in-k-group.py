# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = dummy.next
        
        while curr:
            cnt = 0
            for _ in range(k-1):
                next_node = curr.next
                if next_node is None:
                    break
                curr.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node
                cnt += 1
            
            if cnt != (k-1):
                curr = prev.next
                for _ in range(cnt):
                    next_node = curr.next
                    curr.next = next_node.next
                    next_node.next = prev.next
                    prev.next = next_node
                break
            prev = curr
            curr = curr.next
            

        return dummy.next
                