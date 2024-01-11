# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        res = [0]

        def recursive(node, maxVal, minVal):
            if not node:
                return 0

            if minVal == -1:
                minVal = node.val
            else:
                minVal = min(node.val, minVal)
            if maxVal == -1:
                maxVal = node.val
            else:
                maxVal = max(node.val, maxVal)
            
            recursive(node.right, maxVal, minVal)
            recursive(node.left, maxVal, minVal)
            
            res[0] = max(res[0], abs(node.val - minVal), abs(node.val - maxVal))

        recursive(root, -1, -1)

        return res[0]
        