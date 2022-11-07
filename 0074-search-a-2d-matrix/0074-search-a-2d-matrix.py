class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix),len(matrix[0])
        l,h = 0,n-1
        idx = -1
        while l<=h:
            mid = (l+h)//2
            if matrix[mid][0]<=target and matrix[mid][m-1]>=target:
                idx = mid
                break
            elif matrix[mid][m-1]>target:
                h = mid-1
            else:
                l = mid+1
           
        l,h = 0,m-1
        while l<=h:
            mid= (l+h)//2
            if matrix[idx][mid]==target:
                return 1
            elif matrix[idx][mid]>target:
                h = mid-1
            else:
                l = mid+1
        return 0
        