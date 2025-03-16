from heapq import heappush, heappop, heapify
from collections import Counter
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Using Binary Search
        # min_time = 1
        # max_time = max(ranks) * (cars ** 2)
        # while (min_time <= max_time):
        #     mid = (min_time + max_time) // 2
        #     total_cars_can_repair = 0
        #     for rank in ranks:
        #         total_cars_can_repair += math.floor((mid // rank) ** 0.5) 
        #     if total_cars_can_repair < cars:  
        #         min_time = mid + 1
        #     else:
        #         max_time = mid - 1
        # return min_time
        rank_count = Counter(ranks)
        # This is a min heap which stores the time, rank, cars_repaired, count of ranks with same rank value
        min_heap = [[rank, rank, 1, rank_count[rank]] for rank in rank_count]
        heapify(min_heap)
        while cars > 0:
            time, rank, n, count = heappop(min_heap)
            cars -= count
            n += 1
            heappush(min_heap, [rank * n * n, rank, n, count])
        return time
