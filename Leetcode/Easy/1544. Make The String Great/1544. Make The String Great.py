class Solution:
    def makeGood(self, s: str) -> str:
        good_str = []
        
        res = ""
        for c in s:
            if good_str:
                if c != good_str[-1] and c.lower() == good_str[-1].lower():
                    good_str.pop()
                    continue
            good_str.append(c)
        
        return "".join(good_str)