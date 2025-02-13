class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans = 0
        while nums[0] < k:
            num1 = heapq.heappop(nums)
            num2 = heapq.heappop(nums)
            new_num = num1 * 2 + num2
            heapq.heappush(nums, new_num)
            ans += 1
        return ans