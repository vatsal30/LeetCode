class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i, num_i in enumerate(nums):
            if i > 0 and num_i == nums[i-1]:
                continue
            for j in range(i + 1 , n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                # if j == i+1 and num_j == num_i:
                #     continue
                num_j = nums[j]
                k = j + 1
                l = n - 1
                partial_t = target-(num_j + num_i)
                while k < l:
                    s = nums[k] + nums[l]
                    if s > partial_t:
                        l -= 1
                    elif s < partial_t:
                        k += 1
                    else:
                        ans.append([num_i, num_j, nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
        return ans
                        
                    
