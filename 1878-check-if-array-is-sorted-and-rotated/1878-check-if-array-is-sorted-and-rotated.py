class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = True
        rotateIdx = -1
        for idx in range(1, len(nums)):
            if nums[idx] >= nums[idx-1]:
                continue
            elif flag and nums[idx] < nums[idx-1]:
                rotateIdx = idx
                flag = False
            else:
                return False
        if rotateIdx == -1:
            return True
        if rotateIdx != -1 and nums[-1] <= nums[0]:
            return True
        return False