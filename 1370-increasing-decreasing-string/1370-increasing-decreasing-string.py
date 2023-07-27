class Solution:
    def sortString(self, s: str) -> str:
        a=list(set(s))
        a.sort()
        l=[*s]
        s=''
        for i in range(len(l)):
            for j in a:
                if j in l:
                    s+=j
                    l.remove(j)
            a.reverse()
        return s
        