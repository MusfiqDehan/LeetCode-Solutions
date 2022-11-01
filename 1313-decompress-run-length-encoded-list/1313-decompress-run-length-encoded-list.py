class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(1, len(nums),2):
            arr.extend([nums[i]] * nums[i-1])
        return arr
        