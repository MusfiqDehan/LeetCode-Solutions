class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        math.log(2**31-1)/math.log(3) = 19.558822360291316
        3**19 = 1162261467
        3 is prime number
        '''
        if n == 0 or n < 0:
            return False
        return 1162261467 % n == 0
        