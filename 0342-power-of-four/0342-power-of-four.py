import math

class Solution():
    def isPowerOfFour(self, n):

        if n > 0:
            x = math.log(n,4) 
            return x.is_integer()
        return False 
        