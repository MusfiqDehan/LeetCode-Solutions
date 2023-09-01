class Solution:
    def minOperations(self, n: int) -> int:
        s=t=0
        for i in range(1,n+1):
            if i%2!=0:
                s+=t
                t+=1
            else: 
                s+=t
        return s
        