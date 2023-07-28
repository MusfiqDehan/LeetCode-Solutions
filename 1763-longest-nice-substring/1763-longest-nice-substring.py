class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        #first make a function that check all possiblr substring
        def like(arr):
            f = True
            for i in arr:
                if i.lower() in arr and i.upper() in arr:
                    pass
                else:
                    f = False
            return f
        a = []
        m = ''

        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if like(s[i:j+1]) and len(m)<len(s[i:j+1]):
                    m = s[i:j+1]
        return m
        