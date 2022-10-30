class Solution:
    def averageValue(self, nums: List[int]) -> int:
        evens = []
        
        for i in nums:
            if i%2==0 and i%3==0:
                evens.append(i)
        res = len(evens) and sum(evens)//len(evens)
        
        return res
                