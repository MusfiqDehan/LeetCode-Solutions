# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res=[0]
        def dfs(node):
            if not node: return 0,0
            ls,lc=dfs(node.left)
            rs,rc=dfs(node.right)
            s=ls+rs+node.val
            c=1+rc+lc
            if s//c==node.val: res[0]+=1
            return s,c
        dfs(root)
        return res[0]
        