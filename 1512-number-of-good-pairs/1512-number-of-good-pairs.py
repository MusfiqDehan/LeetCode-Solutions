class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pos = {}
        for i in range(len(nums)):
            if nums[i] not in pos:
                pos[nums[i]] = 1
            else:
                pos[nums[i]] += 1
        print(pos)
        count = 0
        for num in pos:
            if pos[num] >= 2:
                count += (pos[num] * (pos[num]-1)) / 2
        return int(count)

        