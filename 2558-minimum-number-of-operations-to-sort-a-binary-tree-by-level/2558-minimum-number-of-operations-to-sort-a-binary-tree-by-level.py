# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append([root, 0])
        levels = defaultdict(list)
        while queue:
            node, level = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])
        ans = 0
        for level in levels.values():
            sorted_levels = sorted(level)
            pos = { ele: idx for idx, ele in enumerate(level)}
            print(pos)
            for i in range(len(level)):
                if level[i] != sorted_levels[i]:
                    ans += 1
                    cur_pos = pos[sorted_levels[i]]
                    pos[level[i]] = cur_pos
                    level[cur_pos] = level[i]

        return ans