# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        left, right = head, head.next
        while right := right.next:
            right = right.next
            # reverse the first half of the linked list
            left.next.next, left.next, head = head, left.next.next, left.next

        left, right = head, left.next
        ans = head.val + right.val
        while right := right.next:
            # restore linked list
            left.next.next, left.next, head = head, left.next.next, left.next
            ans = max(ans, head.val + right.val)

        return ans
        