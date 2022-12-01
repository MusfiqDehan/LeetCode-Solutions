class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vow = set('aeiouAEIOU')
        
        a = Counter(s[:len(s)//2])
        b = Counter(s[len(s)//2:])
        
        sumA = sum(a[v] for v in vow)
        sumB = sum(b[v] for v in vow)

        return sumA == sumB
        