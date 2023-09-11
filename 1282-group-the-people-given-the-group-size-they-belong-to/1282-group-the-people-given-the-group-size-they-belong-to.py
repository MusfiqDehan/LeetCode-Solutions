class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        for i, group in enumerate(groupSizes):
            if groups[group] and len(groups[group][-1]) < group:
                groups[group][-1].append(i)
            else:
                groups[group].append([i])
        return [i for group in groups.values() for i in group]
        