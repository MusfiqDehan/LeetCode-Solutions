class Solution:
    def removeStars(self, s: str) -> str:
        i=0
        while(i!=len(s)):
            if(s[i]=='*'):
                s=s[:i-1]+s[i+1::]
                i-=1
            else:
                i+=1
        return s