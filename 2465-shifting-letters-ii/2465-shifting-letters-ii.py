class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s_arr = [0] * len(s)
        for shift in shifts:
            i, j, direction = shift
            if direction:
                s_arr[i] += 1 
                if j < len(s) - 1:
                    s_arr[j+1] -= 1
            else:
                s_arr[i] -= 1
                if j < len(s) - 1:
                    s_arr[j+1] += 1
        ans = []
        incr = 0
        print(s_arr)
        for idx, c in enumerate(s):
            incr += s_arr[idx]
            tmp = ((ord(c) - 97) + incr)%26
            
            ans.append(chr(tmp + 97))
        return ''.join(ans)