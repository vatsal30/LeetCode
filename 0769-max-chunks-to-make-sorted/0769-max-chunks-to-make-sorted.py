class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        arr_sum = 0
        idx_sum = 0
        for idx, num in enumerate(arr):
            if idx_sum + idx == arr_sum+num:
                ans += 1
            arr_sum += num
            idx_sum += idx
        return ans
