class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if n<=1:
            return n
        count=1
        maxCount=1
        for i in range(n-1):
            if nums[i+1]-nums[i]==1:
                count+=1
            elif nums[i+1]-nums[i]==0:
                continue
            else:
                count=1
            maxCount=max(maxCount,count)
        return maxCount

        