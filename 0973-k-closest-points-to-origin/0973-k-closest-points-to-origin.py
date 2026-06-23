import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nearests = []
        for point in points:
            heapq.heappush(nearests, (-math.sqrt(point[0] ** 2 + point[1] ** 2), point))
            if len(nearests) > k:
                heapq.heappop(nearests)
        return [point for dist, point in nearests]