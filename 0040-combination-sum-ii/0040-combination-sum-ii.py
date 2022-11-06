class Solution:
    def findCombinations(self, idx, candidates, target, combinations, ds):
        if (target == 0):
            combinations.append(ds.copy())
            return
        for i in range(idx, len(candidates)):
            if (i > idx and candidates[i] == candidates[i-1]):
                continue
            if (candidates[i] > target):
                break
            ds.append(candidates[i])
            self.findCombinations(i+1, candidates, target-candidates[i], combinations, ds)
            ds.pop(-1)
        # self.findCombinations(idx+1, candidates, target, combinations, ds)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        self.findCombinations(0, candidates, target, combinations, [])
        return combinations