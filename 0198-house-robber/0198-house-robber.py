class Solution:
    def rob(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):

            sl = nums[i-2] if i>1 else 0
            l = nums[i-1] if i>0 else 0

            nums[i] = max(sl+nums[i] , l)

        return nums[-1]
        