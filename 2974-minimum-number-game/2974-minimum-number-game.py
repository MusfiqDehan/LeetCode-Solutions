class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)-len(nums)//2):
            a=min(nums)
            nums.remove(a)
            b=min(nums)
            nums.remove(b)
            res.append(b)
            res.append(a)
        return res
        