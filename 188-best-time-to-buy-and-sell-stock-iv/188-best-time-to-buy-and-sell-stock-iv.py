class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        b = [inf] * (k + 1)
        s = [0] * (k + 1)
        for p in prices:
            for k in range(1, k+1):
                b[k] = min(b[k], p - s[k-1])
                s[k] = max(s[k], p - b[k])
        return s[-1]
        