Solution with Extra Space:

**Time Complexity:** `O(n!) * n`

**Space Complexity:** `O(n!) + O(n) + O(n)`

```
class Solution:
    def findPermute(self, nums, answer, map_check, ds):
        if (len(ds) == len(nums)):
            answer.append(ds.copy())
            return
        # print(answer)
        for i in range(len(nums)):
            if (not map_check[i]):
                map_check[i] = 1
                ds.append(nums[i])
                self.findPermute(nums, answer, map_check, ds)
                map_check[i] = 0
                ds.pop(-1)
                
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        map_check = [0] * len(nums)
        self.findPermute(nums, answer, map_check, [])
        return answer
 ```
