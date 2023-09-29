class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        nums2 = sorted(nums)
        
        if nums == nums2 or nums[::-1] == nums2:
            return True
        return False 
        