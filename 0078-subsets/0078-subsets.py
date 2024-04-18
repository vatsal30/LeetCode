class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        self.subsetBacktrack(ans, temp, nums, 0)
        return ans
    
    def subsetBacktrack(self, ans, temp, nums, start):
        ans.append(temp.copy())
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.subsetBacktrack(ans, temp, nums, i + 1)
            temp.pop()
        