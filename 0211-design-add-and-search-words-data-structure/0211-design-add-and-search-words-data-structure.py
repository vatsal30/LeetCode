class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def _find(self, node, start, word):
        for i in range(start, len(word)):
            letter = word[i]
            if letter == '.':
                return any([self._find(child, i + 1, word) for child in node.children.values()])
            elif letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_end

    def search(self, word: str) -> bool:
        return self._find(self.root, 0, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)