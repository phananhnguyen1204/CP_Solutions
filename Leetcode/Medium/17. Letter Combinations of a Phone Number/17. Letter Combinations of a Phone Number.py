class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        def dfs(start, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            candidates = mapping[ord(digits[start]) - ord('0')]
            print(candidates)
            for c in candidates:
                dfs(start + 1, curr + c)
        dfs(0, "")
        return res