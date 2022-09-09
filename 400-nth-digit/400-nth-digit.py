class Solution:
    def findNthDigit(self, n: int) -> int:
        n = n - 1
        
        for digits in range(1, 11):
            first = 10**(digits - 1)
            
            if n < 9 * first * digits:
                return int(str(first + n/digits) [n % digits])
            n = n - (9 * first * digits)
        