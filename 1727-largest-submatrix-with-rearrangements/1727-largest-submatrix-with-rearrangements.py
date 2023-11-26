class Solution:
    def largestSubmatrix(self, G: List[List[int]]) -> int:
        N, M = len(G), len(G[0])
        res = 0
        for r in range(N):
            for c in range(M):
                if r > 0 and G[r][c] != 0:
                    G[r][c] += G[r-1][c]
            sortedRow = sorted(G[r])
            for i in range(M):
                res = max(res, sortedRow[i] * (M-i))
        return res