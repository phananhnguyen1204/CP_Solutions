class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        abc 
        aabc
        abbc

        """
        word_set = set(words)
        words.sort(key = lambda x : -len(x))
        memo = {}
        @cache
        def dfs(curr):
            if curr not in word_set:
                return 0
            if curr in memo:
                return memo[curr]
            curr_chain = 1
            for i in range(len(curr)):
                new_word = curr[:i] + curr[i+1:]
                curr_chain = max(curr_chain, 1 + dfs(new_word))
            memo[word] = curr_chain
            return curr_chain

        res = 0
        for word in words:
            res = max(res, dfs(word))
        
        return res


