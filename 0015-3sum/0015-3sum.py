class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        i = 0
        ans = set()
        while i < N:
            table = set()
            rem = - nums[i]
            j = i + 1

            while j < N:
                if rem - nums[j] in table:
                    ans.add(tuple([nums[i], nums[j], rem-nums[j]]))
                else:
                    table.add(nums[j])
                
                j += 1
            
            while i+1 < N and nums[i] == nums[i+1]:
                i += 1
            i += 1
        
        return list(ans)