class Solution:
    def isPalindrom(self, str):
        left = 0
        right = len(str)-1
        while (left <= right):
            if (str[left] != str[right]):
                return False
            left +=1
            right -= 1
        return True

    def doPartition(self, s, idx, ans, ds):
        if (idx == len(s)):
            ans.append(ds.copy())
            return
        
        for i in range(idx, len(s)):
            if (self.isPalindrom(s[idx:(i+1)])):
                ds.append(s[idx:i+1])
                self.doPartition(s, i+1, ans, ds)
                ds.pop()
            
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.doPartition(s, 0, ans, [])
        return ans