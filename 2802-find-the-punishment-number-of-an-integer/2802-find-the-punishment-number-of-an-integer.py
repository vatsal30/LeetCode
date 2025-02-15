class Solution:
    cache = {}
    def punishmentNumber(self, n: int) -> int:
        def backtrack(num, target):
            if target < 0 or num < target:
                return False
            if num == target:
                return True
            
            return (
                backtrack(num // 10, target - num % 10) or 
                backtrack(num // 100, target - num % 100) or
                backtrack(num // 1000, target - num % 1000)
            )

        ans = 0
        for i in range(1, n+1):
            if i in self.cache:
                ans += self.cache[i]
            else:
                is_true = backtrack(i**2, i)
                if is_true:
                    ans += i**2
                    self.cache[i] = i ** 2
                else:
                    self.cache[i] = 0
        return ans
            