class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        temp=defaultdict(int)
        for i in matches:
            temp[i[0]]=temp[i[0]]
            temp[i[1]]+=1
        
        v=[[],[]]
        for key in temp:
            if temp[key]==0:
                v[0].append(key)
            elif temp[key]==1:
                v[1].append(key)
        
        v[0].sort()
        v[1].sort()
        
        return v