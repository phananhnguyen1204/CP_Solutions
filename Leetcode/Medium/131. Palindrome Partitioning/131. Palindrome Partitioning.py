class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def check_palindrome(s):
            return s == s[::-1]

        def dfs(path, curr):
            if not curr:
                res.append(path[:])
                return
            for i in range(len(curr)):
                if check_palindrome(curr[:i+1]):
                    path.append(curr[:i+1])
                    dfs(path, curr[i+1:])
                    path.pop()
        dfs([], s)
        return res
                    