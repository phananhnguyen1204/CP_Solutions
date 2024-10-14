class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path = path.split("/")

        for dir in path:
            if dir == '..':
                if stack: stack.pop()
            elif dir == '.' or not dir:
                continue
            else:
                stack.append(dir)
        
        return "/" + "/".join(stack)