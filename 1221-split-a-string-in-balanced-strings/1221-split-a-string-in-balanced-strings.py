class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        cnt = 0  
        
        for char in s:
            if char == 'L':
                cnt += 1
            elif char == 'R':
                cnt -= 1
           
            if cnt == 0:
                ans += 1
                
        return ans  
        