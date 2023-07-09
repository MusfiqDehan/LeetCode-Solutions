class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res, lst = 0, []
        for div in set(divisors):
            curr = 0
            for n in nums:
                if not n % div:
                    curr += 1
            if curr > res:
                res = curr
                lst = [div]
            elif curr == res:
                lst.append(div)
        return min(lst)