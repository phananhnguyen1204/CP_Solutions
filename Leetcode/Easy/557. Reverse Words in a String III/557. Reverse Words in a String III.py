class Solution:
    def reverseWords(self, s: str) -> str:
        list_str = s.split(" ")
        res = ""
        for i in range(len(list_str)):
            res += list_str[i][::-1]
            if i == len(list_str) - 1: return res
            res += " "