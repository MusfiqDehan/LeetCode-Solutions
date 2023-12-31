class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxi=-1
        for char in set(s):
            maxi=max(maxi,s.rfind(char)-s.find(char)-1)
        return maxi
        