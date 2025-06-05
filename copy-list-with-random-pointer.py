"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        nodesMap = {}

        curr = head

        while curr:
            if not curr in nodesMap:
                nodesMap[curr] = {}
            nodesMap[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        for key, value in nodesMap.items():
            if key.next != None:
                value.next = nodesMap[key.next]
            if key.random != None:
                value.random = nodesMap[key.random]
        
        return list(nodesMap.values())[0]
