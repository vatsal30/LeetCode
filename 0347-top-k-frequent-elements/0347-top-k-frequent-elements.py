class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_cnt = 0
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
                max_cnt = max(max_cnt, cnt[num])
            else:
                cnt[num] = 1
                max_cnt = max(max_cnt, cnt[num])
        ans = []
        while len(ans) != k:
            for val in cnt:
                if cnt[val] == max_cnt:
                    ans.append(val)
            max_cnt -= 1
        return ans