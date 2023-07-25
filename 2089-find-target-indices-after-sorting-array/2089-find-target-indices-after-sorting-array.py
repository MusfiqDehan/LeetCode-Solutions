class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [index for index, x in enumerate(sorted(nums)) if x == target]
        