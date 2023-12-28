class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:

        maxNum = max(nums)
        maxSum = maxNum
        k -= 1

        while k > 0:
            maxNum += 1
            maxSum += maxNum
            k -= 1
        
        return maxSum
        