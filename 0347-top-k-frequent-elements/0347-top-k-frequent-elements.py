import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        ranked = []
        for num, freq in num_freq.items():
            heapq.heappush(ranked, (freq, num))
            if len(ranked) > k:
                heapq.heappop(ranked)
        ans = []
        while ranked:
            ans.append(heapq.heappop(ranked)[1])

        return ans
