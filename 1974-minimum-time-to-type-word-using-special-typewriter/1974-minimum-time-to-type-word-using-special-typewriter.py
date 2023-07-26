class Solution:
    def minTimeToType(self, word: str) -> int:
        return sum(d if (d:=abs(ord(c)-ord(p)))<13 else 26-d for p,c in pairwise("a"+word))+len(word)
        