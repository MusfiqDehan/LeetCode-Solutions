class Solution(object):
    def maximumCount(self, nums):
        pos = [x for x in nums if x>0]
        neg = [x for x in nums if x<0]
        return max(len(pos),len(neg))
        