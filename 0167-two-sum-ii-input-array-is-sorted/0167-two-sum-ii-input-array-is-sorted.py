class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = len(numbers) - 1

        while idx1 < idx2:
            total = numbers[idx1] + numbers[idx2]
            if total > target:
                idx2 -= 1
            elif total < target:
                idx1 += 1
            else:
                return [idx1 + 1, idx2 + 1]