# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        i = 1
        curr = head
        prev = None

        while i < left:
            prev = curr
            curr = curr.next
            i+=1
        
        orig_prev = prev
        orig_left = curr

        prev = None
        while i <= right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            i+=1
        
        if orig_prev:
            orig_prev.next = prev
        else:
            head = prev
        
        orig_left.next = curr

        return head
        