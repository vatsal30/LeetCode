class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_track = {}
        for value in strs:
            sorted_value = ''.join(sorted(value))
            if sorted_value in anagram_track:
                anagram_track[sorted_value].append(value)
            else:
                anagram_track[sorted_value] = [value]
        return list(anagram_track.values())
        