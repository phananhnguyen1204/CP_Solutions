class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        tmp = "([{"
        for c in s:
            if c in tmp:
                st.append(c)
            elif ((st and st[-1] == "("  and c == ")") 
                or (st and st[-1] == "["  and c == "]") 
                or (st and st[-1] == "{"  and c == "}") ):
                st.pop()
        return not st
            
            