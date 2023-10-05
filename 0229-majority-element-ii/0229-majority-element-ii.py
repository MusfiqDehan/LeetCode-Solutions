class Solution(object):
    def majorityElement(self, nums):
        result = [] 
        x = len(nums)/3
        for num in nums:
            if(nums.count(num) > x):
                if(num not in result): 
                    result.append(num)

        return result

        