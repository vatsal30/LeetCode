class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) -1
        
        while i < len(digits):
        
            digits[i]+=1
            if digits[i] == 10 and i>0:
                digits[i] = 0
                i-=1
                
            elif i == 0 and digits[i] ==10:
                digits.insert(0, 1)
                digits[1] = 0
                
                return digits
            
            else:
                return digits