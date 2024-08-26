class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = nums[0]
        count = 1
        k = 0
        i = 1
        while(i < len(nums)):      
            if (temp == nums[i]):
                count += 1
                if (count > 2):
                    while (i < len(nums)):
                        if (nums[i] == temp):
                            i+=1
                        else:
                            nums[k+1] = nums[i]
                            temp = nums[k+1]
                            k+=1
                            i+=1
                            count = 1
                            break
                else:
                    nums[k+1] = nums[i]
                    k += 1
                    i+=1
                    print(i, k)
                    
            else:
                temp = nums[i]
                nums[k+1] = nums[i]
                k += 1
                count = 1
                i+=1
        return k+1
