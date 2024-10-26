from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.location = defaultdict(list)
        
        for i, word in enumerate(wordsDict):
            self.location[word].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        res = float("inf")

        loc1, loc2 = self.location[word1], self.location[word2]

        i, j = 0, 0
        while i < len(loc1) and j < len(loc2):
            res = min(res, abs(loc1[i] - loc2[j]))
            if loc1[i] < loc2[j]:
                i += 1
            else:
                j += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)