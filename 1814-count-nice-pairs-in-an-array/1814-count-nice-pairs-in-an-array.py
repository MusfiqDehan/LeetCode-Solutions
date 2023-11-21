class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        nums = [int(str(k)[::-1]) - k for k in nums]
        nums = collections.Counter(nums)
        return sum([k*(k-1)//2 for k in nums.values()])%(10**9+7)
        