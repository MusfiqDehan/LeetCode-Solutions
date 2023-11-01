# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = {}
        queue = [root]

        while queue:
            curr = queue.pop()
            dic[curr.val] = dic.get(curr.val, 0) + 1

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
            
        mean = max(dic.values())
        return [k for k, v in dic.items() if v == mean]
        