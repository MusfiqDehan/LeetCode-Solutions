class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse=True)
        for a, b, c in zip(A, A[1:], A[2:]):
            if b + c > a:
                return a + b + c
        return 0
        