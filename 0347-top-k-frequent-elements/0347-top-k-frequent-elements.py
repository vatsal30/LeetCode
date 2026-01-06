class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            num_freq[num] = 1 + num_freq.get(num, 0)
        
        bucket_arr = [[] for _ in range(len(nums) + 1)]

        for num in num_freq:
            bucket_arr[num_freq[num]].append(num)
        
        ans = []
        for i in range(len(bucket_arr) - 1, 0, -1):
            for num in bucket_arr[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
 
        # max_cnt = 0
        # cnt = {}
        # for num in nums:
        #     if num in cnt:
        #         cnt[num] += 1
        #         max_cnt = max(max_cnt, cnt[num])
        #     else:
        #         cnt[num] = 1
        #         max_cnt = max(max_cnt, cnt[num])
        # ans = []
        # while len(ans) != k:
        #     for val in cnt:
        #         if cnt[val] == max_cnt:
        #             ans.append(val)
        #     max_cnt -= 1
        # return ans