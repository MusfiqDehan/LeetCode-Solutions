# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        arr = mountain_arr

        l = 0
        r = arr.length()-1
        cache = {}
        def get_from_cache(index):
            if index not in cache:
                cache[index] = arr.get(index)
            return cache[index]

        while  l <= r:
            mid = l + (r-l)//2

            if mid < arr.length()-1 and mid < arr.length()-1 and get_from_cache(mid) < get_from_cache(mid+1):
                l  = mid +1
            else:
                r = mid - 1
        peak = l 
        l = 0
        r = peak 

        while l <= r:
            mid = l + (r-l)//2
            n =  get_from_cache(mid)
            if n == target:
                return  mid
            elif n < target:
                l = mid + 1
            else:
                r = mid -1
        l = peak
        
        r = arr.length()-1

        while l <= r:
            mid = l + (r-l)//2
            n =  get_from_cache(mid)
            if n == target:
                return  mid
            elif n > target:
                l = mid + 1
            else:
                r = mid -1
        
        

        return -1
        