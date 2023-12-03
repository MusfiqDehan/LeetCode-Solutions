class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for (curr_x, curr_y), (target_x, target_y) in zip(points, points[1:]):
            ans += max(abs(target_x - curr_x), abs(target_y - curr_y))
        
        return ans
        