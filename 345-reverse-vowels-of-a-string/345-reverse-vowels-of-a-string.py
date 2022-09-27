class Solution:
    def reverseVowels(self, s):
        s = list(s)
        
        i = 0
        j = len(s) - 1
        
        vows = set('aeiouAEIOU')
        
        while i < j:
            while i < j and s[i] not in vows: i += 1
            while i < j and s[j] not in vows: j -= 1
            if i > j: break
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
        return ''.join(s)
            