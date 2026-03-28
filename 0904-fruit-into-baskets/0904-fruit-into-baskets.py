from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        left = 0
        right = 0
        unique = Counter() 
        for right in range(len(fruits)):
            unique[fruits[right]] += 1

            while len(unique) > 2:
                unique[fruits[left]] -= 1
                if unique[fruits[left]] == 0:
                    del unique[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

        