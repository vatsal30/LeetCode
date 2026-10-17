from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        left = 0
        ans = 0
        freq = defaultdict(int)
        duplicateCnt = 0
        for right in range(len(nums)):
            freq[nums[right]] += 1
            if freq[nums[right]] == 1:
                k -= 1

            while k < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                    k += 1
                left += 1
                duplicateCnt = 0

            
            if k == 0:
                while freq[nums[left]] > 1:
                    freq[nums[left]] -= 1
                    left += 1
                    duplicateCnt += 1

                ans += duplicateCnt + 1
        return ans
