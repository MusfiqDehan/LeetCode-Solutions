class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        M = max(candies) - extraCandies 
        return [candy >= M for candy in candies]
        