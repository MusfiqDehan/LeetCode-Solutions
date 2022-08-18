# import numpy as np

# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         a = [int(x) for x in str(n)]
#         return np.prod(a) - np.sum(a)



class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summation = 0
        multiplication = 1
        if not n:
            return 0
        while n:
            digit = n % 10
            n = n // 10
            summation += digit
            multiplication *= digit
        return multiplication-summation