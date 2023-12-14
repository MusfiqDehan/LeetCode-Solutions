class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        onesrow = [sum(row) for row in grid]
        onescol = [sum(col) for col in zip(*grid)]
        return [[2 * (onesrow[i] + onescol[j]) - n - m for j in range(n)] for i in range(m)] 