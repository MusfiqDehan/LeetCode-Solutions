# class Solution:
#     def isHappy(self, n):
#         seen = set()
#         while n not in seen:
#             seen.add(n)
#             n = sum([int(x) **2 for x in str(n)])
#         return n == 1


class Solution:
    def isHappy(self, n):
        seen = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in seen:
                return False
            else:
                seen.add(n)
        else:
            return True