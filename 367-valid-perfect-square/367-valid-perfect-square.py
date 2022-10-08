import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt_num = math.sqrt(num)
        
        if num % sqrt_num == 0:
            return True
        else:
            return False
        