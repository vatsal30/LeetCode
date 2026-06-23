import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        klargest = None
        for i in range(k):
            klargest = heapq.heappop(nums)
        return -klargest