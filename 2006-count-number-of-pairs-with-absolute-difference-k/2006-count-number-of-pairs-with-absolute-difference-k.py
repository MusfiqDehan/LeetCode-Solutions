class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        count = Counter(nums)
        for i , j in count.items():
            if i + k in count:
                ans += (count[i] * count[i+k])
        return ans
        