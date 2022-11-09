# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        while curr!=None:
            if curr.val>100000:
                return True
            curr.val+=10000000
            curr=curr.next
        return False