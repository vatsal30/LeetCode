class Solution:
    def decodeString(self, s: str) -> str:
        cs = []
        ds = []
        num = 0
        es = ""
        for c in s:
            if c == '[':
                cs.append(es)
                ds.append(num)
                num = 0
                es = ""
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == "]":
                ps, cnt = cs.pop(), ds.pop()
                es = ps + cnt*es
            else:
                es += c
        return es