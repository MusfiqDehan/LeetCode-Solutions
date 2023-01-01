class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        
        a=len(set(pattern))
        b=len(set(s))
        c=len(set(zip_longest(pattern,s)))
        
        if a==b and b==c:
            return True
        return False