class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        traker = {}
        for value in strs:
            arr = [0]*26
            for val in value:
                arr[ord(val) - 97] += 1
            sig = ""
            for idx, val in enumerate(arr):
                if val > 0:
                    sig += chr(idx + 97)*val
            if sig in traker:
                traker[sig].append(value)
            else:
                traker[sig] = [value]
        return list(traker.values())
        # n*k(logk)
        # anagram_track = {}
        # for value in strs:
        #     sorted_value = ''.join(sorted(value))
        #     if sorted_value in anagram_track:
        #         anagram_track[sorted_value].append(value)
        #     else:
        #         anagram_track[sorted_value] = [value]
        # return list(anagram_track.values())
        