class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)
        res = stack[:-k] if k else stack
        res = ''.join(res).lstrip('0')
        return res if res else '0'