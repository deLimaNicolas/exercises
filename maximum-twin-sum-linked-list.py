# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        res = float("-inf")
        slow = fast = head

        while fast:
            slow = slow.next
            fast = fast.next.next

        reversedHead = self.reverseList(slow)
        
        left, right = head, reversedHead

        while right:
            res = max(res, (left.val + right.val))
            left = left.next
            right = right.next
        
        return res
