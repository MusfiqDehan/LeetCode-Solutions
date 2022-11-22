from math import isqrt

class Solution:
    
    def numSquares(self, n: int, dp = [0]) -> int:

        for k in range(len(dp), n+1):
            if k == len(dp) : dp.append(inf)
            for i in range(1, isqrt(k)+1):
                dp[k] = min(dp[k], 1 + dp[k - (i*i)])
                
        return dp[n]
        