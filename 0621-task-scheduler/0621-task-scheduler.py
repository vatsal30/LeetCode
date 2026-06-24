from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_counts = sum(1 for count in counts.values() if count == max_freq)
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_counts)
        # Heap Task schedular approach
        # counts = [0] * 26
        # for task in tasks:
        #     counts[ord(task) - ord('A')] += 1

        # counts = [-val for val in counts if val > 0]
        # heapq.heapify(counts)
        # interval = 0
        # queue = deque()
        # while counts or queue:
        #     interval += 1
        #     while queue and queue[0][0] < interval:
        #         heapq.heappush(counts, queue.popleft()[1])
        #     if counts:
        #         freq = heapq.heappop(counts)
        #         if freq + 1 < 0:
        #             queue.append((interval + n, freq+1))
        # return interval
            
            