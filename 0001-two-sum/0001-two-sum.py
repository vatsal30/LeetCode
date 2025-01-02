class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict ={}
        for idx, val in enumerate(nums):
            if (numDict.get(val)==None):
                numDict[val] = [idx]
            else:
                numDict[val].append(idx)
        for x in numDict:
            y = target - x
            y_val = numDict.get(y)
            if (y_val!= None):
                if (x==y and len(y_val) > 1):
                    return [y_val[0], y_val[1]]
                elif(x!=y):
                    return [numDict[x][0], y_val[0]]
                