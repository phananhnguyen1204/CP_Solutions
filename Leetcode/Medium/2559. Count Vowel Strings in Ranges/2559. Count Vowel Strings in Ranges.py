class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix = [0] * n
        vowels = "aeiou"

        def check(word):
            return word[0] in vowels and word[-1] in vowels
        for i, word in enumerate(words):
            add = 1 if check(word) else 0
            if i == 0: prefix[i] = add
            else:
                prefix[i] = prefix[i - 1] + add

        res = []
        for l, r in queries:
            if l == 0:
                res.append(prefix[r])
            else:
                res.append(prefix[r] - prefix[l - 1])
        
        return res