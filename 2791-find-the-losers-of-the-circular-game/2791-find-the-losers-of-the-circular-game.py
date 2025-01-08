from functools import reduce
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        players = [0] * n
        players[0] = 1
        i = 1
        curr = 0
        while True:
            curr = (curr + i * k) % n
            if players[curr] == 1:
                break
            players[curr] = 1
            i += 1
        ans = []
        for i in range(n):
            if players[i] == 0:
                ans.append(i+1)
        return ans