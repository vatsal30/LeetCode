class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            i = i.lower()
            order_i = ord(i)
            if ((order_i >= 48 and order_i <= 57) or (order_i >= 97 and order_i<=122)):
                new_s += i
        left = 0
        right = len(new_s) - 1
        while (left < len(new_s)//2 and right >= len(new_s)//2):
            if (new_s[left] != new_s[right]):
                return False
            left += 1
            right -= 1
        return True