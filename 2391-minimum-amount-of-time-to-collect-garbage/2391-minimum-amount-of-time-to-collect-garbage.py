class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        currTimeG = 0
        currTimeP = 0
        currTimeM = 0
        travel = [0] + travel
        maxTimeM, maxTimeP, maxTimeG = 0, 0, 0
        for i, char in enumerate(garbage):
            currTimeG += travel[i]
            currTimeP += travel[i]
            currTimeM += travel[i]
            if char.count('G') > 0:
                maxTimeG = char.count('G') + currTimeG
                currTimeG = maxTimeG
            if char.count('P') > 0:
                maxTimeP = char.count('P') + currTimeP
                currTimeP = maxTimeP
            if char.count('M') > 0:
                maxTimeM = char.count('M') + currTimeM
                currTimeM = maxTimeM
        return (maxTimeM + maxTimeG + maxTimeP)
        