class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(0) 		#Adding a zero to the end of the list in order to avoid the index going beyond the acceptable limits at the end of the algorithm.
        pivot, left, right = 0, 0, sum(nums[1:])
        while(pivot < n):
            if(left == right):
                return pivot
            else:
                left += nums[pivot]
                right -= nums[pivot + 1]
                pivot += 1
        return -1
        