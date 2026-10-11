from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        freq = defaultdict(int)
        ans = 0
        for num3 in nums3:
            for num4 in nums4:
                freq[num3 + num4] += 1
        
        for num1 in nums1:
            for num2 in nums2:
                ans += freq[-(num1 + num2)]
        return ans

