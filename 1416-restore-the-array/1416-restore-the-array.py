class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        @cache
        def dp(i):
            if i == len(s): return 1
            num = cnt = 0
            for j in range(i, len(s)):
                num = num * 10 + int(s[j])
                if num == 0 or num > k:
                    break
                cnt += dp(j + 1)
            return cnt % (10**9 + 7)
        return dp(0)
        