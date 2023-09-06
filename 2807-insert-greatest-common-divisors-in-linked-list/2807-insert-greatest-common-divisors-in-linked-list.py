# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def gcd(a, b):
    if b == 0: return abs(a)
    return gcd(b, a % b)

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        node = head
        
        while node and node.next:
            temp = ListNode()
            temp.val = gcd(node.val, node.next.val)
            temp.next = node.next
            node.next = temp
            node = node.next.next
        return head 
        