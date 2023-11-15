class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum_i = 0
        for i in range(len(nums)):
            if str(bin(i)).count("1") == k:
                sum_i += nums[i]
        return sum_i
        