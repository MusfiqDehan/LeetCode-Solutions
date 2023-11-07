class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        dist = [math.ceil(dist[i]/speed[i]) for i in range(len(dist))]
        dist.sort()
        i = 0
        while i<len(dist):
            if dist[i]-i<=0:
                break
            i += 1
        return i