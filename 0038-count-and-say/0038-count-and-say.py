class Solution:
    def mapFunc(self, s):
        ans = []
        p = s[0]
        c = 1
        for i in range(1, len(s)):
            if (s[i] == p):
                c+=1
            else:
                ans.append([str(c), p])
                p = s[i]
                c = 1
        ans.append([str(c), p])
        return ans

    def countAndSay(self, n: int) -> str:
        if (n==1):
            return "1"
        else:
            return ''.join([item for sublist in self.mapFunc(self.countAndSay(n-1)) for item in sublist])
        