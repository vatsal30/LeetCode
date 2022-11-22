class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        nums = []
        for i in range(1, n):
            fact *= i
            nums.append(i)
        nums.append(n)
        
        ans = ""
        k = k-1
        while(True):
            ans = ans + str(nums[(k//fact)])
            nums.pop(k//fact)
            if (len(nums) == 0):
                return ans
            k = k % fact
            fact = fact // len(nums)