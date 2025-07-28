class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        
    def search(self, word: str) -> bool:
        def check(root, word):
            if not word:
                return root.word

            if word[0] != ".":
                if word[0] not in root.children:
                    return False
                else:
                    return check(root.children[word[0]], word[1::])
            else:
                for children in root.children.values():
                    if check(children, word[1::]):
                        return True 
                return False
        
        return check(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
