class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for i in sorted(nums):
            if original == i:
                original *= 2
        return original
        