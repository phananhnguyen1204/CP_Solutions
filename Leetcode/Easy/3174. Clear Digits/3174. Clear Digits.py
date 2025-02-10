class Solution:
    def clearDigits(self, s: str) -> str:
        """
        doing operation repeatedly 
        -> whenever see digit, if its adjacent is not digit -> remove
        -> use stack
        """
        
        stack = []

        for c in s:
            if c.isdigit():
                if stack: stack.pop()
            else:
                stack.append(c)

        return "".join(stack)