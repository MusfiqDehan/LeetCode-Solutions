class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse=True)
        for a, b, c in zip(A, A[1:], A[2:]):
            if b + c > a:
                return a + b + c
        return 0
    
# class Solution(object):
#     def largestPerimeter(self, A):
#         A.sort()
#         for i in xrange(len(A) - 3, -1, -1):
#             if A[i] + A[i+1] > A[i+2]:
#                 return A[i] + A[i+1] + A[i+2]
#         return 0
        