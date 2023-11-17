class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)-1
        i=0
        s=[]
        while(i<n):
            s.append(nums[i]+nums[n])
            i+=1
            n-=1
        return max(s)
        