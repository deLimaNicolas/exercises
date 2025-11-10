class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        pairs = zip(word, word[::-1])

        for s, e in pairs:
            if (s, e) not in curr.children:
                curr.children[(s, e)] = TrieNode()
            curr = curr.children[(s, e)]
            curr.count += 1
        return curr.count

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        ans = 0
        for i in range(len(words) - 1, -1, -1):
            word = words[i]
            count = trie.insert(word)
            if count > 1:
                ans += (count - 1)
        return ans
