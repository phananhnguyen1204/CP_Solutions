class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, curr_len = [], 0
        for i in range(len(words)):
            if len(line) + len(words[i]) + curr_len > maxWidth:
                extra_space = maxWidth - curr_len
                spaces = extra_space // max(1, len(line) - 1)
                remainder = extra_space % max(1, len(line) - 1)
                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                res.append("".join(line))
                #Reset
                line, curr_len = [], 0
            #line completed
            line.append(words[i])
            curr_len += len(words[i])
        # Handle lastline
        last_line = " ".join(line)
        trailing = maxWidth - len(last_line)
        res.append(last_line + " " * trailing)
        return res
