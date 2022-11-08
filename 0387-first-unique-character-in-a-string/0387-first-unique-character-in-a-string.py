class Solution:
    def firstUniqChar(self, s: str) -> int:
        a_dict = {}
        
        for i in s:
            if i not in a_dict:
                a_dict[i]=1
            else:
                a_dict[i]+=1
                
        index= -1
        
        for i in range(len(s)):
            if a_dict[s[i]]== 1:
                index= i
                break     
        return index
        
        