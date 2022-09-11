class Solution:
    def romanToInt(self, s: str) -> int:
        conversions = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000           
        }
        
        s = s.replace("IV", "IIII").replace("IX", "VIIII") # 4, 9        
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX") # 40, 90
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC") # 400, 900
        
        sum = 0
        for char in s:
            sum += conversions[char]
        
        return sum
            
        