# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def _height(node):
            if not node:
                return 0
            l,r = _height(node.left),_height(node.right)
            if abs(l-r) > 1:
                return float('inf')
            return 1+max(_height(node.left),_height(node.right))
        if _height(root) == float('inf'):
            return False
        return True
        