# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkOpposite(self,lRoot,rRoot):
        if rRoot == None and lRoot == None:
            return True
        if (rRoot and lRoot )== None:
            return False
        
        if rRoot.val == lRoot.val:
            return self.checkOpposite(lRoot.left, rRoot.right) and self.checkOpposite(lRoot.right,rRoot.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None or (root.left == None and root.right != None) or (root.left != None and root.right == None):
            return False
        lRoot = root.left
        rRoot = root.right

        return self.checkOpposite(lRoot,rRoot)
        