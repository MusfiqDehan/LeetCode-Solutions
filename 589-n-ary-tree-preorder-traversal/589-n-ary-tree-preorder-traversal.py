"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        output =[]
        
        self.dfs(root, output)
        
        return output
    
    def dfs(self, root, output):
        if root is None:
            return
        
        output.append(root.val)
        
        for child in root.children:
            self.dfs(child, output)
       
        