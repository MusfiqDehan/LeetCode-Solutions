class Solution:
    def countPoints(self, rings: str) -> int:
        map = {}
        for i in range(0, len(rings), 2):
            if rings[i+1] not in map:
                map[rings[i+1]] = set(rings[i])
            else:
                map[rings[i+1]].add(rings[i])

        count = 0
        for k,v in map.items():
            if len(v) == 3:
                count += 1

        return count
        