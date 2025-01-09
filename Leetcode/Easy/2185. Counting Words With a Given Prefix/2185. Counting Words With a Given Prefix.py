class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for word in words:
            if word.find(pref) == 0:
                cnt += 1

        return cnt