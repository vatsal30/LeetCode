class Solution:
    def findPermute(self, idx, nums, answer):
        if (idx == len(nums)):
            answer.append(nums.copy())
            return
        # print(answer)
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.findPermute(idx+1, nums, answer)
            nums[idx], nums[i] = nums[i], nums[idx]
            
                
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.findPermute(0, nums, answer)
        return answer
        