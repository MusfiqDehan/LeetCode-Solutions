class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [1] * n

        for i in range(0,n,1):
            max_seq_at_i = 1
            for j in range(0,i,1):
                #print ("i,j,nums[i], nums[j]", i, j, nums[i], nums[j])
                current_seq = 0
                if nums[i] > nums[j]:
                    current_seq = dp[j] + 1
                if current_seq > max_seq_at_i:
                    max_seq_at_i = current_seq
            dp[i] = max_seq_at_i
        
        return(max(dp))
        
        