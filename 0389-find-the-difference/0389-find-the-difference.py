class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = Counter(s)
        
        for char in t:
            counts[char] -= 1
            if counts[char] < 0:
                return char
        