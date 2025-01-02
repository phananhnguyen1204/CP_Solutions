class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dfs(x, n):
            if n == 0: return 1
            if x == 0: return 0

            res = dfs(x, n // 2)
            return x * res * res if n % 2 == 1 else res * res

        res = dfs(x, abs(n))
        return res if n >= 0 else 1 / res