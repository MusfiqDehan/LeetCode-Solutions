class Solution:
    def minDeletions(self, s: str) -> int:
        dic = collections.Counter(s)
        ans = 0
        temp = []
        for i in dic:
            while dic[i] > 0 :
                if dic[i] in temp:
                    ans += 1
                    dic[i]-=1
                else:
                   temp.append(dic[i])
                   break        
        return ans
        