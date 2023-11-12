class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        l = len(pref)
        for i in range(l-1):
            ans.append(pref[i]^pref[i+1])
        return ans