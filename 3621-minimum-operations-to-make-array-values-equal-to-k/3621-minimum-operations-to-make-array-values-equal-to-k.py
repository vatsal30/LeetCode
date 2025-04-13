class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        sorted_freq = sorted(freq.items())
        if sorted_freq[0][0] < k:
            return -1
        return len(sorted_freq) if sorted_freq[0][0] > k else len(sorted_freq) - 1
            
        