class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "*":
                stack.append(c)
            else:
                if stack: stack.pop()
        return "".join(stack)