class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        count_1 = 0
        res = 0

        for item in s:
            if item =='1':
                count_1 += 1

            else:
                res = min(res+1, count_1)

        return res