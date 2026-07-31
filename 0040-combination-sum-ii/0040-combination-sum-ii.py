class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result, combination = [], []
        candidates.sort()
        def backtrack(start, k):
            if k == 0:
                result.append(combination[:])
                return
            if k < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                combination.append(candidates[i])
                backtrack(i + 1, k - candidates[i])
                combination.pop()
        backtrack(0, target)
        return result
            