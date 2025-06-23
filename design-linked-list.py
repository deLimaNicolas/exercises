class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:
    def __init__(self):
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next

        while curr != self.tail:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
            
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val, self.head.next, self.head)
        self.head.next.prev = newNode
        self.head.next = newNode

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val, self.tail, self.tail.prev)
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return 
            
        i = 0
        curr = self.head.next
        
        while curr != self.tail:
            if i == index:
                newNode = ListNode(val, curr, curr.prev)
                curr.prev.next = newNode
                curr.prev = newNode
                return
            curr = curr.next
            i += 1
            
        if i == index:
            self.addAtTail(val)
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
            
        i = 0
        curr = self.head.next  
        
        while curr != self.tail:
            if i == index:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                return 
            curr = curr.next
            i += 1
