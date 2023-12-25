# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr=[]

        def tree(root1):

            if root1 is not None:
                tree(root1.left)
                arr.append(root1.val)
                tree(root1.right)
     
        tree(root1)
        tree(root2)

        arr.sort()

        return arr    