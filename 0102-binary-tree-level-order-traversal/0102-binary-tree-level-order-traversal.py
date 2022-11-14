# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        nodes_list = [(root, False, 0)]
        
        traversal_order_list = []
        
        while nodes_list:
            node, visited, level = nodes_list.pop()
            if node:
                if visited:
                    try:
                        traversal_order_list[level].append(node.val)
                    except Exception as err:
                        traversal_order_list.append([])
                        traversal_order_list[level].append(node.val)
                else:
                    nodes_list.append((node.right, False, level+1))
                    nodes_list.append((node.left, False, level+1))
                    nodes_list.append((node, True, level))
        return traversal_order_list