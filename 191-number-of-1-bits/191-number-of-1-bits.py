# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         convert_string = str(n)        
#         for i in convert_string:
#             if i == '1':
#                 count += 1
                
#         return count


class Solution:
     def hammingWeight(self, n: int) -> int:
            return bin(n).count('1')