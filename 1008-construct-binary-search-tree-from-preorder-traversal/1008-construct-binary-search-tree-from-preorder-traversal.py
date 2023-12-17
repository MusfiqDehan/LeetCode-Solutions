# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        node = preorder[0]
        root = TreeNode(node)
        low = [i for i in preorder if i < node]
        high = [i for i in preorder if i > node]

        root.left = self.bstFromPreorder(low)
        root.right = self.bstFromPreorder(high)

        return root 
        