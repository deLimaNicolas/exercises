class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char] 
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        visited = set()

        for word in words:
            trie.addWord(word)
        
        res = []
        ROW, COL = len(board), len(board[0])

        def dfs(pos, trieNode, word): # Time complexity = O(m * n * 4pow(L) +s)
            r, c = pos
            if(
                r < 0 or c < 0 or
                r >= ROW or c >= COL or
                pos in visited or
                board[r][c] not in trieNode.children
            ):
                return
            
            visited.add(pos)
            word += board[r][c]
            trieNode = trieNode.children[board[r][c]]
            
            if trieNode.word:
                res.append(word)
                trieNode.word = False
            
            dfs((r + 1, c), trieNode, word)
            dfs((r - 1, c), trieNode, word)
            dfs((r, c + 1), trieNode, word)
            dfs((r, c - 1), trieNode, word)
            
            visited.remove(pos)

        for row in range(ROW):
            for col in range(COL):
                visited = set()
                dfs((row, col), trie.root, "")

        return res
