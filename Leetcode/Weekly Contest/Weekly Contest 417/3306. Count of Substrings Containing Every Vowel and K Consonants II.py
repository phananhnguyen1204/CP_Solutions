class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        res = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        def helper(word, k):
            freq = {}
            res = 0
            cnt = 0
            l = 0
            for r in range(len(word)):
                if word[r] in vowels:
                    freq[word[r]] = freq.get(word[r], 0) + 1
                else:
                    cnt += 1
                while l <= r and cnt >= k and len(freq) == 5:
                    res += len(word) - r
                    if word[l] in vowels:
                        freq[word[l]] -= 1
                        if freq[word[l]] == 0:
                            del freq[word[l]]
                    else:
                        cnt -= 1
                    l += 1
            return res
        return helper(word, k) - helper(word, k + 1)