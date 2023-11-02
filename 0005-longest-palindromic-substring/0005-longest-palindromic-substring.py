class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        def check(l,r,s):
            nonlocal res
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
        for i in range(len(s)):
            check(i,i,s)
            check(i,i+1,s)
        return res
        