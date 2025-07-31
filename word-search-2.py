class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None  # Store the actual word here when we reach the end

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert a word into the trie. Basic stuff."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.word = word  # Store the complete word

class Solution:
    def findWords(self, board, words):
        """
        The CORRECT way to solve Word Search II.
        Step 1: Build trie from words (not from board, genius)
        Step 2: DFS on board while traversing trie
        Step 3: Profit
        """
        if not board or not board[0] or not words:
            return []
        
        # Step 1: Build trie from the word list
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        rows, cols = len(board), len(board[0])
        result = set()  # Use set to avoid duplicates
        
        def dfs(row, col, node, visited):
            """
            DFS that actually makes sense.
            We traverse the board AND the trie simultaneously.
            """
            # Boundary checks
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                (row, col) in visited):
                return
            
            # Get current character
            char = board[row][col]
            
            # If this character isn't in our trie, no point continuing
            if char not in node.children:
                return
            
            # Move to next trie node
            next_node = node.children[char]
            
            # If we found a complete word, add it to results
            if next_node.is_end:
                result.add(next_node.word)
                # Don't return here! We might find longer words
            
            # Mark as visited and continue DFS
            visited.add((row, col))
            
            # Explore all 4 directions
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                dfs(row + dr, col + dc, next_node, visited)
            
            # Backtrack - remove from visited
            visited.remove((row, col))
        
        # Try starting DFS from every cell
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, trie.root, set())
        
        return list(result)
