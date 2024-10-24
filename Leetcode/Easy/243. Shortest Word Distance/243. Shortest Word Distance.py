class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i, j = -1, -1
        res = len(wordsDict)
        for idx, word in enumerate(wordsDict):
            if word == word1:
                i = idx
            elif word == word2:
                j = idx

            if i != -1 and j != -1:
                res = min(res, abs(i - j))
        
        return res