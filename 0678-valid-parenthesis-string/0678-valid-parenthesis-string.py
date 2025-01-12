class Solution:
    def checkValidString(self, s: str) -> bool:
        openStack = []
        starStack = []
        for idx, letter in enumerate(s):
            if letter == '(':
                openStack.append(idx)
            elif letter == '*':
                starStack.append(idx)
            elif letter == ')' and openStack:
                openStack.pop()
            elif letter == ')' and starStack:
                starStack.pop()
            else:
                return False
        while openStack and starStack and openStack[-1] < starStack[-1]:
            openStack.pop()
            starStack.pop()
        if openStack:
            return False
        return True
