class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                curr.children[i] = Node()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(root, word):
            curr = root
            for j in range(len(word)):
                c = word[j]
                if c == '.':
                    for i in range(26):
                        if curr.children[i] and dfs(curr.children[i], word[j+1:]):
                            return True
                    return False
                else:
                    i = ord(c) - ord('a')
                    if not curr.children[i]:
                        return False
                    curr = curr.children[i]          
            return curr.end
        return dfs(self.root, word)

        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)