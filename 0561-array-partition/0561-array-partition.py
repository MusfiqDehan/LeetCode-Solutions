class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[a] for a in range(0,len(nums), 2)])
        