# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def search(root,visited):
            if not root:
                return False
            if k - root.val in visited:
                return True
            visited.add(root.val)
            return search(root.left,visited) or search(root.right,visited)
        
        return search(root,set())
        