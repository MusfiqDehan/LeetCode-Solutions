class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def text(s):
            while '#' in s:
                k = s.index('#')
                if k == 0:
                    s = s[1:]
                else:
                    s = s[:k-1] + s[k+1:]
            return s
        return text(s) == text(t) 
        