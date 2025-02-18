class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(arr, counter):
            if len(arr) == len(nums):
                ans.append(arr.copy())
                return
            for num in counter:
                if counter[num] > 0:
                    arr.append(num)
                    counter[num] -= 1
                    backtrack(arr, counter)
                    arr.pop()
                    counter[num] += 1


        backtrack([], Counter(nums))
        return ans