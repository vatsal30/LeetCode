class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            if curr_sum > target:
                right -= 1
            else:
                left += 1