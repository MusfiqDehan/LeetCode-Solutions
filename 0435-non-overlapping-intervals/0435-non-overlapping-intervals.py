class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1]))

        n = len(intervals)
        ans = 0
        c = intervals[0][1]

        for i in range(n - 1):
            if c > intervals[i + 1][0]:
                ans += 1
            else:
                c = intervals[i + 1][1]
        return ans