class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        new_queries = [[] for _ in heights]
        for idx, (a, b) in enumerate(queries):
            if a == b:
                ans[idx] = b
            elif a > b and heights[a] > heights[b]:
                ans[idx] = a
            elif a < b and heights[a] < heights[b]:
                ans[idx] = b
            else:
                new_queries[max(a, b)].append((max(heights[a], heights[b]), idx))

        max_index = []
        for idx, height in enumerate(heights):
            while max_index and max_index[0][0] < height:
                _, query_idx = heappop(max_index)
                ans[query_idx] = idx
            for ele in new_queries[idx]:
                heappush(max_index, ele)
        return ans

    def leftmostBuildingQueriesLinearSolution(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        for idx in range(len(queries)):
            if queries[idx][0] > queries[idx][1]:
                queries[idx][0], queries[idx][1] = queries[idx][1], queries[idx][0]
        sorted(queries, key = lambda x: x[1])
        ans = []
        for a, b in queries:
            if a == b or heights[a] < heights[b]:
                ans.append(b)
            else:
                ans.append(-1)
                for i in range(b + 1, len(heights)):
                    if heights[i] > heights[a]:
                        ans[-1] = i
                        break
        return ans

                