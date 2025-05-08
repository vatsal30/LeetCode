from heapq import heappush, heappop
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        que = []
        heappush(que, (0, 0, 0, 1))
        end = (len(moveTime) - 1, len(moveTime[0]) - 1)
        DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = [[0] * len(moveTime[0]) for _ in range(len(moveTime))]
        while que:
            time, x, y, time_cost = heappop(que)
            if (x, y) == end:
                return time 
            if visited[x][y]:
                continue
            visited[x][y] = 1
            for direction in DIRECTIONS:
                nx, ny = x + direction[0], y + direction[1]
                if 0 <= nx <= end[0] and 0 <= ny <= end[1]:
                    new_time = max(time, moveTime[nx][ny]) + time_cost
                    new_time_cost = 2 if time_cost == 1 else 1
                    heappush(que, (new_time, nx, ny, new_time_cost))
            


        