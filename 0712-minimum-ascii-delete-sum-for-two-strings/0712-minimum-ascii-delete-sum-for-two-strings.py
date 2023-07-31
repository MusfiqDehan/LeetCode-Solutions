class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        totalSum = 0
        for c in s1:
            totalSum += ord(c)

        for c in s2:
            totalSum += ord(c)

        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1]) + ord(s2[j - 1])

                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return totalSum - dp[-1][-1]
        