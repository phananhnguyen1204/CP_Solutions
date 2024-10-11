class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, cnt_open, cnt_close):
            if cnt_open + cnt_close == 2 * n:
                if cnt_open == cnt_close:
                    res.append(curr)
                    return
            if cnt_open > n: return
            dfs(curr + "(", cnt_open + 1, cnt_close)
            if cnt_open > cnt_close:
                dfs(curr + ")", cnt_open, cnt_close + 1)
        
        dfs("", 0, 0)
        return res