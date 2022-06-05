class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        
        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False
        
#         temp_nums = nums
#         set_nums = list(set(temp_nums))
        
#         if temp_nums == set_nums:
#             return True
#         return False
        