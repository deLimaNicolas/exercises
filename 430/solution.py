"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def get_tail(curr):
            while curr:
                prev = curr
                curr = curr.next

            return prev
        dummy = Node(0, None, head)

        curr = dummy.next

        while curr:
            if curr.child:
                child_tail = get_tail(curr.child)
                child_tail.next = curr.next
                if curr.next:
                    curr.next.prev = child_tail
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
            curr = curr.next
        
        return dummy.next

