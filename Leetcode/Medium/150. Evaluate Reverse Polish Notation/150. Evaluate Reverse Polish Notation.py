class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "*/+-":
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    num2 += num1
                    stack.append(num2)
                elif token == "/":
                    stack.append(int(num2 / num1))
                elif token == "-":
                    num2 -= num1
                    stack.append(num2)
                else:
                    stack.append(num1 * num2)
            else:
                stack.append(int(token))
        return stack[-1]