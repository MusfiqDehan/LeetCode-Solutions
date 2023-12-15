class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        citiesA = set()
        
        for path in paths:
            citiesA.add(path[0])
        for path in paths:
            if path[1] not in citiesA:
                return path[1]
        