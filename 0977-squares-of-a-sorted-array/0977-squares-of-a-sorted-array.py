class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_sqr = [i**2 for i in nums]
        return sorted(nums_sqr)
        