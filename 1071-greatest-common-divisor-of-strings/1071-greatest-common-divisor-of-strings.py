class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1=len(str1)
        n2=len(str2)
        st=""
        s=""
        ct=0
        for i in range(min(n1,n2)):
            if str1[i]!=str2[i]:
                break
            s+=str1[i]
            ct+=1
            if n1%ct==0 and n2%ct==0:
                if s*(n1//ct)==str1 and s*(n2//ct)==str2:
                    st=s
        return st