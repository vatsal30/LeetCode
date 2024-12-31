class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day_to_travel = days[-1]
        travel_costs = [0] + [0] * last_day_to_travel
        ptr = 0
        for i in range(1, len(travel_costs)):
            if days[ptr] == i:
                travel_costs[i] = min(
                    travel_costs[i - 1] + costs[0],
                    travel_costs[max(0, i - 7)] + costs[1],
                    travel_costs[max(0, i - 30)] + costs[2],
                )
                ptr += 1
            else:
                travel_costs[i] = travel_costs[i - 1]
        return travel_costs[-1]
