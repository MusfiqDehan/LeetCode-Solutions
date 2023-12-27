class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res=0
        s=""
        nt=neededTime
        t=[]
        for i in range(len(colors)):
            if(len(s)>0 and s[-1]==colors[i]):
                if(len(t)>0 and t[-1]<nt[i]):
                    res+=t[-1]
                    t.pop()
                    t.append(nt[i])
                else:
                    res+=nt[i]
            else:
                s+=colors[i]
                t.append(nt[i])
        return res
        