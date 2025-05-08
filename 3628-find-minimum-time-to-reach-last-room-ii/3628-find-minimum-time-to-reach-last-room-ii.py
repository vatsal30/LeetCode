from heapq import heappush, heappop
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        que = []
        heappush(que, (0, 0, 0, 0))
        time_cost = (1, 2)
        end = (len(moveTime) - 1, len(moveTime[0]) - 1)
        DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        while que:
            time, x, y, time_cost_idx = heappop(que)
            if (x, y) == end:
                return time 
            if (x, y, time_cost_idx) in visited:
                continue
            visited.add((x, y, time_cost_idx))
            for direction in DIRECTIONS:
                nx, ny = x + direction[0], y + direction[1]
                if 0 <= nx <= end[0] and 0 <= ny <= end[1]:
                    new_time = max(time, moveTime[nx][ny]) + time_cost[time_cost_idx] 
                    heappush(que, (new_time, nx, ny, (time_cost_idx + 1) % 2))
            


        