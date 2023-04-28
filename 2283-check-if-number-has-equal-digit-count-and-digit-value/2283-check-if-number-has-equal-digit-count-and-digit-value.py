class Solution:
    def digitCount(self, num: str) -> bool:
        d = {}
        for n in num:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        return all(d.get(str(i), 0)==int(num[i]) for i in range(len(num)))
        