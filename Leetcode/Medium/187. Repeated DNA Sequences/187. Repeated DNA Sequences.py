class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        seen, res = set(), set()
        for i in range(n - 9):
            tmp = s[i : i + 10]
            if tmp in seen:
                res.add(tmp)
            seen.add(tmp)
        return list(res)