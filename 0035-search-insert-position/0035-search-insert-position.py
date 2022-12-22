class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        for (i, v) in enumerate(nums):
            if v >= target:
                return i
            
        return len(nums)
            
        