class Solution:
    # def sumOddLengthSubarrays(self, A):
    #     res, n = 0, len(A)
    #     for i, a in enumerate(A):
    #         res += ((i + 1) * (n - i) + 1) // 2 * a
    #     return res
    
     def sumOddLengthSubarrays(self, A):
            return sum(((i + 1) * (len(A) - i) + 1) // 2 * a for i, a in enumerate(A))
