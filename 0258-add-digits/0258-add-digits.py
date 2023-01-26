class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)

        while len(s) > 1:
            total = 0
            for i in s:
                total += int(i)
            s = str(total)
            
        num = int(s)
        
        return num