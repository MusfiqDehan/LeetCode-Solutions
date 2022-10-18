class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum([a.count('*') for a in s.split('|')][0::2])
        