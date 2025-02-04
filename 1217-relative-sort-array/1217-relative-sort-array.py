class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        freq = Counter(arr1)
        for num in arr2:
            num_freq = freq[num]
            ans.extend([num] * num_freq)
            del freq[num]
        for num in sorted(freq.keys()):
            ans.extend([num] * freq[num])
        return ans