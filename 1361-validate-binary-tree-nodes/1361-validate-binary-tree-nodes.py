class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        visited = set()
        q = [] # root to start
        for i in range(n):
            if i not in leftChild and i not in rightChild:
                q.append(i)

        if len(q) > 1: 
            return False

        while q:
            index = q.pop(0)

            if index in visited:
                return False

            visited.add(index)

            if leftChild[index] >= 0:
                q.append(leftChild[index])

            if rightChild[index] >= 0:
                q.append(rightChild[index])

        return True if len(visited) == n else False
        