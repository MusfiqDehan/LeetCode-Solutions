# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == [] : 
            return 
        root = max(nums)
        rootIndex = nums.index(root)
        left = nums[:rootIndex]
        right = nums[rootIndex + 1:]
        return TreeNode(val = root, left = self.constructMaximumBinaryTree(left), right = self.constructMaximumBinaryTree(right))
        