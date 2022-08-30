class Solution:
    def plusOne(self, digits):
        s = [str(integer) for integer in digits]
        
        a_string = "".join(s)

        res = int(a_string)+1
        
        res = [int(x) for x in str(res)]
        
        return res
    