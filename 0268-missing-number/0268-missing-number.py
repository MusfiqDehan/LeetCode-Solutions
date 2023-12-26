class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nmax = max(nums)
        S = (nmax+1)*nmax//2
        x = S-sum(nums)
        if len(nums)==nmax+1 and x==0:
            return nmax+1
        return x
        