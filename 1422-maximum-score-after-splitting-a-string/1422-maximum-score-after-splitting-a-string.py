class Solution:
    def maxScore(self, s: str) -> int:
        m=0
        for i in range(1,len(s)):
            st=l=list(map(int, s.strip()))
            l=(st[:i])
            r=(st[i:])
            l=len(l)-sum(l)
            r=sum(r)
            sm=(l+r)
            m=max(sm,m)
        return m
        