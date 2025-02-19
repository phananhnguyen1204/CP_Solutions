class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        brute force works
        """
        letters = ["a", "b", "c"]
        res = []

        curr = []
        def dfs(prev):
            if len(curr) == n:
                res.append("".join(curr.copy()))
                return

            for letter in letters:
                if letter != prev:
                    curr.append(letter)
                    dfs(letter)
                    curr.pop()
        dfs("")
        res.sort()
        return "" if len(res) < k else res[k-1]



        