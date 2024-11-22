class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = 0
        self.cnt = 0

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = Node()
            curr = curr.children[idx]
            curr.cnt += 1
        curr.end += 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                return 0
            curr = curr.children[idx]
        return curr.end
        

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                return 0
            curr = curr.children[idx]
        return curr.cnt

    def erase(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            curr = curr.children[idx]
            curr.cnt -= 1
        curr.end -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)