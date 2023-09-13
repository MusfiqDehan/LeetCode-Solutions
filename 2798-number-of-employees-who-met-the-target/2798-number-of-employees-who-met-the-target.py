class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        k = 0
        for i in hours:
            if i >= target:
                k+=1
        return k