class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, combination = [], []
        def backtrack(idx, target):
            if target == 0:
                result.append(combination[:])
                return
            elif target < 0:
                return
            for i in range(idx, len(candidates)):  
                combination.append(candidates[i])
                backtrack(i, target - candidates[i])
                combination.pop()
        backtrack(0, target)
        return result