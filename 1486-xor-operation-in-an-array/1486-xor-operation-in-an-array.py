class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        res = 0
        
        nums = [start + n * 2 for n in range(n)]
        
        for n in nums:
            res = res ^ n
            
        return res 