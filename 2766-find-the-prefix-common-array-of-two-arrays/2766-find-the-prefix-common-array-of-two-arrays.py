class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = [0] * len(A)
        ans = [0] * len(A)
        for idx in range(len(A)):
            ans[idx] = ans[idx - 1]
            freq[A[idx] - 1] += 1
            if freq[A[idx] - 1] == 2:
                ans[idx] += 1
            freq[B[idx] - 1] += 1
            if freq[B[idx] - 1] == 2:
                ans[idx] += 1
        return ans