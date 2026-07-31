class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DIGIT_MAP = { 
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"], 
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }
        result = []
        def backtrack(start, comb):
            if start == len(digits):
                result.append(comb)
                return
            for c in DIGIT_MAP[digits[start]]:
                backtrack(start + 1, comb + c)
            
                    
        backtrack(0, "")
        return result