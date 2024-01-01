class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        ans = 0

        g.sort()
        s.sort()
        i = 0
        j = 0

        while i < len(s) and j < len(g):

            if s[i] >= g[j]:
                ans += 1
                i += 1
                j += 1

            else:
                i += 1

        return ans
        