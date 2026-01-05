class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        track_char = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in track_char:
                track_char[char] += 1
            else:
                track_char[char] = 1
        for char in t:
            if char in track_char and track_char[char] > 0:
                track_char[char] -= 1
            else:
                return False
        return True