# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast,prev=head,head,None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if prev==None:
            return None
        prev.next=slow.next
        return head
        