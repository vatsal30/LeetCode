class Solution:
    def findCombinations(self, ind, candidates, target, combinations, ds):
        if (ind == len(candidates)):
            if (target == 0):
                combinations.append(ds.copy())
            return 
        if (candidates[ind] <= target):
            ds.append(candidates[ind])
            self.findCombinations(ind, candidates, target-candidates[ind], combinations, ds)
            ds.pop(-1)
        self.findCombinations(ind+1, candidates, target, combinations, ds)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        self.findCombinations(0, candidates, target, combinations, [])
        return combinations