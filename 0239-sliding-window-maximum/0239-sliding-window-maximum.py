class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        l, r = 0, 0
        ans = []
        q = deque()

        while r < N:
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if ((r - l) + 1) == k:
                ans.append(nums[q[0]])
                l += 1
            
            if l > q[0]:
                q.popleft()
            
            r += 1
        
        return ans
