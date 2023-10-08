class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)-1
        def recursivepro(prepro, i):
            nonlocal nums, n
            if i>n:
                return 1
            postpro = recursivepro(prepro*nums[i], i+1)
            temp = nums[i]
            nums[i] = prepro*postpro
            return temp*postpro

        recursivepro(1,0)
        return nums
        