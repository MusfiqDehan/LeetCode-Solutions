# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, {})
    def dfs(self, root, freqs):
        # print("freqs", freqs)
        freq_copy = freqs.copy()
        if root.val in freq_copy:
            freq_copy[root.val] += 1
        else:
            freq_copy[root.val] = 1
        # print("copy", freq_copy)
        if not root.left and not root.right:
            # print("leaf", root.val)
            freq = freq_copy.values()
            odd_freq = 0
            # print(list(freq))
            for each in freq:
                if each % 2 != 0:
                    if odd_freq >= 1:
                        return 0
                    odd_freq += 1
            return 1
        left = right = 0
        if root.left:
            left = self.dfs(root.left, freq_copy)
        if root.right:
            right = self.dfs(root.right, freq_copy)
        return left + right