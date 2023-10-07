class Solution(object):
    def prefixCount(self, words, pref):
        l =len(pref)
        count = 0
        
        for i in words:

            if i[:l] == pref:
                count +=1
        return count
        