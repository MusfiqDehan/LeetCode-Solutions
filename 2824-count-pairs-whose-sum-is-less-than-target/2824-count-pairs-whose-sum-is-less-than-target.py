class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        x = 0
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                x = nums[i]+nums[j]
                if x < target:
                    count+=1
        return count
        