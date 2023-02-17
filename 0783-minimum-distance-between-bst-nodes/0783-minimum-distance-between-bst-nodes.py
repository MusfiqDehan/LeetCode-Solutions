# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        arr = []
        def inorder(root, arr):
            if root is None: return
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)
        mini = float('inf')
        inorder(root, arr)
        for i in range(len(arr)-1):
            mini = min(mini, arr[i+1] - arr[i])
        return mini