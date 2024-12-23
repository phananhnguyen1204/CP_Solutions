class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s, start, end):
            while start <= end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        def reverse_each_word(s):
            start = end = 0
            while end < len(s):
                while end < len(s) and s[end] != " ":
                    end += 1
                
                reverse(s, start, end - 1)
                end += 1
                start = end
        
        reverse(s, 0, len(s) - 1)
        reverse_each_word(s)