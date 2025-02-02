class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = True
        rotateIdx = True
        for idx in range(1, len(nums)):
            if nums[idx] >= nums[idx-1]:
                continue
            elif flag and nums[idx] < nums[idx-1]:
                rotateIdx = False
                flag = False
            else:
                return False
        if not rotateIdx and nums[-1] <= nums[0]:
            return True
        return rotateIdx