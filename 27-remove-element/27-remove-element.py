class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while True:
        #     try:
        #         nums.remove(val)
        #     except:
        #         break
        # return len(nums)
        
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
        