class Solution:
     def reorderedPowerOf2(self, N):
        return sorted(str(N)) in [sorted(str(1 << i)) for i in range(30)]
        