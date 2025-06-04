# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        if not list1:
            return list2
        if not list2:
            return list1

        newHead = list2
        checkpoint = list1 
        if list1.val <= list2.val:
            newHead = list1
            checkpoint = list2

        curr = newHead

        while curr:
            tmp = curr
            if not curr.next:
                curr.next = checkpoint
                break
            if curr.next.val <= checkpoint.val:
                curr = curr.next
            else:
                tmp = curr.next
                curr.next = checkpoint
                checkpoint = tmp
                curr = curr.next
        return newHead
