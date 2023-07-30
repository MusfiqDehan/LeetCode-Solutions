# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def increasingBST(self, root):
        resnode=TreeNode(0)
        orderednode=resnode
        arr=[]
        def inorder(node):
            if not node:
                return
            else:
                inorder(node.left)
                arr.append(node.val)
                inorder(node.right)
        inorder(root)
        for i in arr:
            new=TreeNode(i)
            resnode.left=None
            resnode.right=new
            resnode=resnode.right
        return orderednode.right
        