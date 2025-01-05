class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # memo[i]: is it possible to build substring from index 0th till ith index.
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i < 0:
                return True

            for word in wordDict:
                if s[i - len(word) + 1 : i + 1] == word and dfs(i - len(word)):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return dfs(len(s) - 1)
