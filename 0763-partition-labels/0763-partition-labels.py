class Solution(object):
    def partitionLabels(self, s):

        ind = {}
        for i, c in enumerate(s):
            if c in ind:
                ind[c][1] = i
            else:
                ind[c] = [i,i]
        ans = []
        i = 0
        while i < len(s):
            j = i
            last = ind[s[i]][1]
            while j < last:
                if ind[s[j]][1]>last:
                    last = ind[s[j]][1]
                j += 1
            ans.append(last-i+1)
            i = last + 1
        return ans
        