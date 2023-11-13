class Solution(object):
    def finalString(self, s):
        ans = ""
        for i in s:
            if i=="i":
                ans = ans[::-1]
            else:
                ans += i
        return ans
        