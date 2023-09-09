class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        dp[0]=1
        n=len(nums)

        for i in range(target+1):
            for j in range(n):
                if i>=nums[j]:
                    dp[i]+=dp[i-nums[j]]
        # print(dp)
        return dp[-1]
        