class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        combined = "".join( (s[1:], s[:-1]) )
        return s in combined
        