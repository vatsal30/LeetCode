class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s_arr = [0] * (len(s) + 1)
        for shift in shifts:
            i, j, direction = shift
            s_arr[i] += (2 * direction - 1)
            s_arr[j+1] -= (2 * direction - 1)
        ans = list(s)
        incr = 0
        for idx, c in enumerate(s):
            incr += s_arr[idx]
            ans[idx] = chr((((ord(c) - 97) + incr)%26) + 97)
        return ''.join(ans)