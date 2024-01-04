class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = defaultdict(lambda:0)
        for i in nums:
            d[i]+=1

        ans = 0
        for i in d:
            if d[i]==1:return -1
            ans += d[i]//3 + min(1,d[i]%3)
        return ans
        