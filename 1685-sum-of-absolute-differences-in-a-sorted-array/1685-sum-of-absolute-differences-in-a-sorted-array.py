class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        d = []
        l = len(nums)
        t = sum(nums)
        s = 0
        for i in range(l):
            n = nums[i]
            d.append(n*(2*i - l) + t - s)
            s += 2 *n 
        return d
