class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        def check(word, pattern):
            if len(pattern) > len(word): return False
            for i in range(len(pattern)):
                if pattern[i] != word[i]: return False
            
            return True
        
        for i, word in enumerate(sentence.split()):
            if check(word, searchWord): return i + 1
        
        return -1