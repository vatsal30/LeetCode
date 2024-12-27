class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = float("-inf")
        max_i_pair = values[0]
        for i in range(1, len(values)):
            if values[i] - i + max_i_pair > ans:
                ans = values[i] - i + max_i_pair
            if i + values[i] > max_i_pair:
                max_i_pair = i + values[i]
        return ans