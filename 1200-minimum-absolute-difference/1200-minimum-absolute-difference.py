from collections import defaultdict
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        sol = defaultdict(list)
        min_diff = float("inf")
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            min_diff = min(diff, min_diff)
            sol[diff].append([arr[i-1], arr[i]])
        return sol[min_diff]
        