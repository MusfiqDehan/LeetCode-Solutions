class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        return sum(map(max, zip(*map(sorted, grid))))
        