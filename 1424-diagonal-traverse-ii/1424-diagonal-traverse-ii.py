class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag_elements = []
        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                diag_elements.append((i + j,j,num))
        diag_elements.sort()
        return [element[2] for element in diag_elements]        
        