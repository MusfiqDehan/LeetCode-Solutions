class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        max_len = len(bin(max(a, b, c)))
        ans = 0
        

        def stringify(num: int, max_len: int) -> str:
            num = bin(num)[2:].rjust(max_len, '0')
            return num
        

        c = stringify(c, max_len)
        b = stringify(b, max_len)
        a = stringify(a, max_len)

        for i in range(max_len):
            ai, bi, ci = int(a[i]), int(b[i]), int(c[i])
            if ci == 1:
                if ai + bi >= 1:
                    pass
                else:
                    ans += 1
            if ci == 0:
                if ai != bi:
                    ans += 1
                if ai == bi == 1:
                    ans += 2

        return ans
        