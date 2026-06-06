# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        """
            a. If there is no right child, return the left child. This effectively deletes the current node by bypassing it.
            b. If there is no left child, return the right child. This effectively deletes the current node by bypassing it.
            c. If there are both left and right children, find the minimum larger node (min_right_node) by traversing down the left side of the right subtree. This is the node with the smallest value that is still larger than self.val.
            Replace self.val with min_right_node.val.
            d. Delete min_right_node.val from the right subtree and set the right child to the return value of the recursive call.
            e. Return the current node.
        """
        curr = root
        dummy = TreeNode()
        dummy.left = root
        prev = dummy
        while curr:
            
            if curr.val > key:
                prev = curr
                curr = curr.left
            elif curr.val < key:
                prev = curr
                curr = curr.right
            else:
                if curr.right and curr.left:
                    min_right_node = curr.right
                    while min_right_node.left:
                        min_right_node = min_right_node.left
                    curr.val = min_right_node.val
                    curr.right = self.deleteNode(curr.right, min_right_node.val)
                elif not curr.right:
                    if prev.left == curr:
                        prev.left = curr.left
                    else:
                        prev.right = curr.left
                else:
                    if prev.left == curr:
                        prev.left = curr.right
                    else:
                        prev.right = curr.right

                break
            
            
        return dummy.left
        