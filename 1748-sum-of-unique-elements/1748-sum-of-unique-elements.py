class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
        m =[]
        for i in l:
            if nums.count(i) == 1:
                m.append(i)
        s = sum(m)
        return s