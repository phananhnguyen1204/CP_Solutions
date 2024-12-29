class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbreviation = defaultdict(set)
        
        for word in dictionary:
            self.abbreviation[self.get_key(word)].add(word)

    def get_key(self, word):
        if len(word) <= 2: return word
        key =  "".join([word[0], str(len(word) - 2), word[-1]]) 
        print(key)
        return key

    def isUnique(self, word: str) -> bool:
        key = self.get_key(word)
        if key not in self.abbreviation: return True
        if word in self.abbreviation[key] and len(self.abbreviation[key]) == 1: return True
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)