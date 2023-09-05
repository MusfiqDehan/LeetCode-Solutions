"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        hashtable = { None: None }

        curr_dummy = Node(0,head)
        copy_dummy = Node(0,None)

        curr = curr_dummy
        copy = copy_dummy

        while curr.next:
            copy.next = Node(curr.next.val)

            curr = curr.next
            copy = copy.next

            hashtable[curr] = copy

        curr = curr_dummy
        copy = copy_dummy

        while curr.next:
            curr = curr.next
            copy = copy.next

            copy.random = hashtable[curr.random]

        return copy_dummy.next
        