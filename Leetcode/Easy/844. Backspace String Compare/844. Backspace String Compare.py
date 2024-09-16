class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def solve(s):
            cnt = 0
            res = ""
            for i in range(len(s) - 1, -1, -1):
                if s[i] == "#":
                    cnt += 1
                else:
                    if cnt > 0: cnt-= 1
                    else: res += s[i]
            return res[::-1]
        return solve(s) == solve(t)
                        