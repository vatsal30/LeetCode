class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        freq = Counter()
        l1 = len(nums1)
        l2 = len(nums2)
        for num in nums1:
            freq[num] += l2
        
        for num in nums2:
            freq[num] += l1
        
        ans = 0
        for num, occ in freq.items():
            if occ % 2 == 1:
                ans ^= num
        return ans