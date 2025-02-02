class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        dirCount = Counter()
        dist = 0
        max_dist = float("-inf")
        for c in s:
            dirCount[c] += 1
            dist += 1
            min_x = min(dirCount['W'], dirCount['E'])
            min_y = min(dirCount['N'], dirCount['S'])
            max_dist = max(max_dist, dist - 2 * max(0, min_x + min_y - k))
        return max_dist
        