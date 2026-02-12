from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        for idx, val in enumerate(nums):
            while dq and nums[dq[-1]] < val:
                dq.pop() 
            dq.append(idx)

            if (idx + 1) >= k:
                while dq and dq[0] < (idx - k + 1):
                    dq.popleft()
                ans.append(nums[dq[0]])    
        return ans