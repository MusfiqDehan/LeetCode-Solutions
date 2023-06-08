class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([num < 0 for sublist in grid for num in sublist])

        