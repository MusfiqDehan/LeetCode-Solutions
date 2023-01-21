class Solution:
    def fib(self, n):
        if n==0:
            return 0
        if n==1:
            return 1

        ans = [0,1]
        for i in range(n-2):
            ans.append(ans[i]+ans[i+1])

        return ans[-1] + ans[-2]