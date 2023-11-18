class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, left, operation = 0, 0, 0
        for right in range(1, len(nums)):
            operation += (nums[right] - nums[right-1]) * (right-left)
            if operation > k:
                operation -= nums[right] - nums[left]
                left += 1
            else:        
                ans = max(right - left, ans)
        return ans + 1  
        