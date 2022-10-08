# TimeComplexity O(n*k)
# space complexity O(n*k)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            l = [0] * 26
            for c in s:
                l[ord(c) - ord('a')] += 1
            d[tuple(l)].append(s)
        return d.values()
    
    
''' 
#-> Time Complexity O(n*k*log(k))
#-> space Complexity O(n*k)
class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for i in strs:
            sorted_str = ''.join(sorted(i))
            print(sorted_str)
            if sorted_str not in d:
                d[sorted_str] = [i]
            else:
                d[sorted_str].append(i)
        
        return list(d.values())
'''