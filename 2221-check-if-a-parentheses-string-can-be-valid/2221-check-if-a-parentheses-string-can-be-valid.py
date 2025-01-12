class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        unlocked = 0
        openP = 0
        for i in range(len(s)):
            if locked[i] == '0':
                unlocked += 1
            elif s[i] == '(':
                openP += 1
            elif s[i] == ')':
                if openP:
                    openP -= 1
                elif unlocked:
                    unlocked -= 1
                else:
                    return False
        balanced = 0
        for i in range(len(s)-1, -1, -1):
            if locked[i] == '0':
                unlocked -= 1
                balanced -= 1
            elif s[i] == '(':
                openP -= 1
                balanced += 1
            elif s[i] == ')':
                balanced -= 1
            if balanced > 0:
                return False
            if openP == 0 and unlocked == 0:
                break
        if openP > 0:
            return False
        return True