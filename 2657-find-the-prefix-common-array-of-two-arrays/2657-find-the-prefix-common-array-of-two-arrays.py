class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        n = len(A)
        SA = set()
        SB = set()
        for i in range(0, n):
            SA.add(A[i])
            SB.add(B[i])
            common = SA & SB
            res.append(len(common))
        return res