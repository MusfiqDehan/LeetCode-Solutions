class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        s = []
        sm = 0
        for num in satisfaction:
            sm += num
            if sm >= 0:
                s.append(num)
        s.sort()
        return max(0, sum(num*(i+1) for i, num in enumerate(s)))
        