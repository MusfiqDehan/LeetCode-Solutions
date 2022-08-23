class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sol = []
        dic1 = {}
        dic2 = {}
        for i,v in enumerate(nums1):
            dic1[v] = i
        for i,v in enumerate(nums2):
            dic2[v] = i
        for v1 in dic1:
            for v2 in dic2:
                k = dic2[v1]
                if v2 > v1 and dic2[v2] > k:
                    sol.append(v2)
                    break
                if dic2[v2] == len(nums2)-1:
                    sol.append(-1)
        return sol
