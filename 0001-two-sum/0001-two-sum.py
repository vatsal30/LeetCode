class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in num_dict:
                return [num_dict[diff], idx]
            else:
                num_dict[num] = idx
        # for idx, num in enumerate(nums):
        #     diff = target - num
        #     if diff in num_dict:
        #         if diff == num and len(num_dict[diff]) > 1:
        #             return num_dict[diff]
        #         elif diff != num:
        #             return [idx, num_dict[diff][0]]
                

            