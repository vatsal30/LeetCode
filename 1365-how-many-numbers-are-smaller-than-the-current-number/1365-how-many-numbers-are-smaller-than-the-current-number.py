class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ordered = sorted(nums)
        ans = []
        for num in nums:
            cnt = 0
            while num > ordered[cnt]:
                cnt += 1
            ans.append(cnt)
        return ans