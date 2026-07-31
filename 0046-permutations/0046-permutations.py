class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(perm, used):
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            for idx, num in enumerate(nums):
                if not used[idx]:
                    perm.append(num)
                    used[idx] = 1
                    backtrack(perm, used)
                    perm.pop()
                    used[idx] = 0
        backtrack([], [0] * len(nums))
        return result