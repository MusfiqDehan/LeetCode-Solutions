class Solution:
    # bin function
    
    # def sortByBits(self, A):
    #     return sorted(A, key=lambda a: [bin(a).count('1'), a])
    
    # Bit manipulation
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda num : (sum((num >> i) & 1 for i in range(32)), num))
        