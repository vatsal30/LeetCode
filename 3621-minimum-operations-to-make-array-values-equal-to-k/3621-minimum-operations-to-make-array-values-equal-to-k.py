class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        lookup_table = {}
        for num in nums:
            if num < k:
                return -1
            if num in lookup_table:
                continue
            elif num > k:
                lookup_table[num] = 1
                ans += 1
            else:
                lookup_table[num] = 1
        return ans
            
        