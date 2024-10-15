class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                tmp = ""
                while stack and stack[-1] != '[':
                    tmp = stack.pop() + tmp
                stack.pop()
                multiply = ""
                while stack and stack[-1].isdigit():
                    multiply = stack.pop() + multiply

                stack.append(int(multiply) * tmp)
        return "".join(stack)
