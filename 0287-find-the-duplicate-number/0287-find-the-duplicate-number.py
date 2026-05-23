class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        curr = 0
        while nums[slow] != nums[curr]:
            curr = nums[curr]
            slow = nums[slow]
        return nums[curr]