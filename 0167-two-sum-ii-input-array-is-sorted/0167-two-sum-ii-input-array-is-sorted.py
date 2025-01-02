class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1 = 0
        ptr2 = len(numbers) - 1
        while ptr1 < ptr2:
            s = numbers[ptr1] + numbers[ptr2]
            if s == target:
                return [ptr1 + 1, ptr2 + 1]
            elif s < target:
                ptr1 += 1
            else:
                ptr2 -= 1