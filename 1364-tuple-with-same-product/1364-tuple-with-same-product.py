class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prodFreq = Counter()
        n = len(nums)
        for idx in range(n):
            for idx2 in range(idx + 1, n):
                prodFreq[nums[idx] * nums[idx2]] += 1
        ans = 0
        for freq in prodFreq.values():
            if freq > 1:
                # It will be we need to get two paris from x pairs which gives us the product
                # so it will be xC2 = x!/((x-2)!*2!)
                # which is equivalent to x * (x-1) / 2
                # and for each 2 pairs we can rearrange them in 8 different pairs
                # so final ans would be x * (x - 1) * 8 / 2
                ans += freq * (freq-1) * 4
        return ans

