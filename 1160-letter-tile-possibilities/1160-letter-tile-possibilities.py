class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = 0
        def backtrack(arr, counter):
            nonlocal ans
            if len(arr) == len(tiles):
                return
            for c in counter:
                if counter[c] > 0:
                    arr.append(c)
                    counter[c] -= 1
                    ans += 1
                    print(arr)
                    backtrack(arr, counter)
                    arr.pop()
                    counter[c] += 1

        backtrack([], Counter(tiles))
        return ans


        backtrack('', Counter(tiles))