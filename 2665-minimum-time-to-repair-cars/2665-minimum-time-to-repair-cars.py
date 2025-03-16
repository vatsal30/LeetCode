class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_time = 1
        max_time = max(ranks) * (cars ** 2)
        while (min_time <= max_time):
            mid = (min_time + max_time) // 2
            total_cars_can_repair = 0
            for rank in ranks:
                total_cars_can_repair += math.floor((mid // rank) ** 0.5) 
            if total_cars_can_repair < cars:  
                min_time = mid + 1
            else:
                max_time = mid - 1
        return min_time
