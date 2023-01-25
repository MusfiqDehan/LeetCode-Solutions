class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        nums_element = sum(nums)
        nums_digit = "".join(str(i) for i in nums)
        nums_digit = [int(i) for i in nums_digit]
        nums_digit = sum(nums_digit)
        
        return abs(nums_element - nums_digit)