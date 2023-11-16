import random
class Solution(object):
    def findDifferentBinaryString(self, nums):
        while True:
            s = len(nums[0])
            se = ''
            for i in range(s):
                se+= str(random.randint(0,1))
            if se not in nums:
                return se
        