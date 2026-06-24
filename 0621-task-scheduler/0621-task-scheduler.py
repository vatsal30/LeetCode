from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord('A')] += 1

        counts = [-val for val in counts if val > 0]
        heapq.heapify(counts)
        interval = 0
        queue = deque()
        while counts or queue:
            interval += 1
            while queue and queue[0][0] < interval:
                heapq.heappush(counts, queue.popleft()[1])
            if counts:
                freq = heapq.heappop(counts)
                if freq + 1 < 0:
                    queue.append((interval + n, freq+1))
        return interval
            
            