class Solution:
    def sortVowels(self, s: str) -> str:
        vow = ['a','e','i','o','u','A','E','I','O','U']
        x = []
        y = []
        for i in s :
            x.append(i)
            if i in vow :
                y.append(i)
        ptr = 0
        y = sorted(y)
        for i in range(len(x)):
            if x[i] in vow :
                x[i] = y[ptr]
                ptr+=1
        return ''.join(x)
        