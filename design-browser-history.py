class Page:
    def __init__(
        self, 
        page, 
        next=None, 
        prev=None
        ):

        self.page = page
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head, self.tail = Page(""), Page("")
        self.head.next, self.tail.prev = self.tail, self.head
        
        homePage = Page(homepage, self.tail, self.head)
        self.head.next = homePage
        self.tail.prev = homePage
        self.lastSeen = homePage
        
    def visit(self, url: str) -> None:
        newPage = Page(url, self.tail, self.lastSeen)
        self.lastSeen.next = newPage
        self.tail.prev = newPage
        self.lastSeen = newPage
        
    def back(self, steps: int) -> str:
        i = 0
        curr = self.lastSeen

        while curr != self.head and i < steps:
            curr = curr.prev
            i += 1
            
        if curr == self.head:
            curr = self.head.next  # Can't go before homepage
            
        self.lastSeen = curr
        return curr.page
        
    def forward(self, steps: int) -> str:
        i = 0
        curr = self.lastSeen

        while curr != self.tail and i < steps:
            curr = curr.next
            i += 1
            
        if curr == self.tail:
            curr = self.tail.prev  # Can't go past last visited
            
        self.lastSeen = curr
        return curr.page

