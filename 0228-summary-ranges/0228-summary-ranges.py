class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l=len(nums)
        if l==0:
            return []
        start=0
        ans=[]
        for i in range(l):
            if i+1<l and nums[i]+1 == nums[i+1]:
                continue
            elif start==i:
                ans.append(str(nums[i]))
                start=i+1
            else:
                ans.append(str(nums[start])+"->"+str(nums[i]))
                start=i+1
        return ans
        