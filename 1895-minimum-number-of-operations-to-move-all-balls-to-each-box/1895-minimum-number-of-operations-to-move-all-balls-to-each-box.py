class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        reverse_sum = [0] * n
        total_box = int(boxes[n-1])
        for idx in range(n-2, -1, -1):
            reverse_sum[idx] = reverse_sum[idx + 1] + total_box
            total_box += int(boxes[idx])
        ans = []
        total_box = 0
        l_sum = 0
        for idx, box in enumerate(boxes):
            l_sum = l_sum + total_box
            ans.append(l_sum + reverse_sum[idx])
            total_box += int(boxes[idx])


        return ans