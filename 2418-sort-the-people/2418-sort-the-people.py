class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = []
        for i in range(len(names)):
            result.append([heights[i], names[i]])
        result = sorted(result, reverse=True)
        return [name for height, name in result]
            
        