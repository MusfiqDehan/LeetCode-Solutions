class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        x=len(nums)
        res=set()

        def rec(i,lst):
            if len(lst)>1:
                res.add(tuple(lst))

            if i==x:
                return

            if not lst or lst[-1]<=nums[i]:
                rec(i+1,lst+[nums[i]])

            rec(i+1,lst)

        rec(0,[])

        return res