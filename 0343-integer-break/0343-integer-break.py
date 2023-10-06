class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return n-1
        
        ans=n//3
        r=n%3
        
        if r==1:
            return 3**(ans-1)*2*2
        if r==2:
            return 3**(ans)*2
        return 3**ans
        