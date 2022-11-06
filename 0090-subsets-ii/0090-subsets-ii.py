class Solution:
    def generateSubset(self, idx, arr, subsets, subset):
        if (idx == len(arr)):
            # subsets.append(subset.copy())
            return
        for i in range(idx, len(arr)):
            if (i>idx and arr[i]==arr[i-1]):
                continue
            
            subset.append(arr[i])
            subsets.append(subset.copy())
            self.generateSubset(i+1, arr, subsets, subset)
            subset.pop(-1)
            
            # self.generateSubset(i+1, arr, subsets, subset)
            
            
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums.sort()
        self.generateSubset(0, nums, subsets, [])
        return subsets