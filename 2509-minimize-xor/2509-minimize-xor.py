class Solution:
    def count_bits(self, num):
        bits = 0
        while num > 0:
            bits += num & 1
            num = num >> 1
        print(bits)
        return bits

    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt1, cnt2 = self.count_bits(num1), self.count_bits(num2)
        ans = num1
        idx = 0
        while cnt1 != cnt2:
            if cnt1 > cnt2 and (ans & (1 << idx)):
                ans = ans ^ (1 << idx)
                cnt1 -= 1
            if cnt1 < cnt2 and not (ans & (1 << idx)):
                ans = ans | (1 << idx)
                cnt1 += 1
            idx += 1
        return ans
        