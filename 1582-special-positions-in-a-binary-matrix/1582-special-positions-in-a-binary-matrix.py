class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        answer = 0

        def check(x, y):
            for j in range(n):
                if y != j and mat[x][j]:
                    return 0
            for i in range(m):
                if x != i and mat[i][y]:
                    return 0
            return 1
                
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    answer += check(i, j)

        return answer
        