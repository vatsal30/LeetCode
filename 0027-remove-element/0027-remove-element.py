class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums) - 1
        idx = 0
        if n == -1:
            return 0
        while n >= 0 and nums[n] == val:
            n -= 1
        while idx <= n:
            if nums[idx] == val:
                nums[idx], nums[n] = nums[n], nums[idx]
                while n >= 0 and nums[n] == val:
                    n -= 1
                print(idx, n)
            idx += 1
        return n + 1