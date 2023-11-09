class Solution:
    def countHomogenous(self, s: str) -> int:
        def count(n):
            return (n*(n+1))//2
        l,r=0,1
        prev=s[0]
        ans=0
        while r<len(s):
            if s[r]==prev:
                r+=1
            else:
                ans+=count(r-l)
                prev=s[r]
                l=r
                r+=1
        if l<len(s):
            ans+=count(r-l)
        return ans%(10**9+7)
        