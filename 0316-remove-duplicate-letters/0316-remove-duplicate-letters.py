class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ans=[]
        
        for i in range(len(s)):
            if s[i] not in ans:
                j=len(ans)-1
                while(j>=0 and ans[j]>s[i] and ans[j] in s[i+1:] ):
                    ans.pop()
                    j=j-1
                ans.append(s[i])
        ans="".join(ans)
        return ans
        