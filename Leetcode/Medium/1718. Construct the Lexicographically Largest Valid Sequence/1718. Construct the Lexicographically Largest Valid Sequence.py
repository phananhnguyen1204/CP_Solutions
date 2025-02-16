class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """
        len of sequence = 2 * n - 1
        1 must be in sequence
        brute force + greedy: generate all permuation
        try to use max integer first -> first answer found is the lexicographically largest
        """

        res = [0] * (2 * n - 1)
        used = set()

        def backtrack(i):
            if i == len(res):
                return True
            for num in range(n, -1, -1):
                if num in used: continue
                if num > 1 and (i + num >= len(res) or res[i + num] != 0): continue

                used.add(num)
                res[i] = num
                if num > 1:
                    res[i + num] = num
                next_idx = i + 1
                while next_idx < len(res) and res[next_idx] != 0:
                    next_idx += 1
                if backtrack(next_idx):
                    return True
                used.remove(num)
                res[i] = 0
                if num > 1:
                    res[i + num] = 0
            return False

        backtrack(0)
        return res