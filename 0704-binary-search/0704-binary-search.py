class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute Force
        
        # for i, v in enumerate(nums):
        #     if v == target:
        #         return i
        # return -1
    
        # Binary Search
        
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (l + r) // 2 
            # m = (0+5) // 2 = 2.5 = 2
            
            if nums[m] > target: 
                # nums[2] = 3 > 9
                
                r = m - 1
            elif nums[m] < target:
                # nums[2] = 3 < 9
                l = m + 1 
                # m = 2+1=3+1=4 
                # nums[2]=3, nums[3]=5, nums[4]=9
                
            else:
                # nums[m] == target
                # 9 == 9
                return m
            
        return -1
                
        