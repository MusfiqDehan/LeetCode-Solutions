# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def height(p):
            if not p: return -1       
                            
            left, right = height(p.left), height(p.right)
            self.ans = max(self.ans, 2+left+right)   
            
            return 1+max(left, right)
            
        height(root)
        return self.ans
        