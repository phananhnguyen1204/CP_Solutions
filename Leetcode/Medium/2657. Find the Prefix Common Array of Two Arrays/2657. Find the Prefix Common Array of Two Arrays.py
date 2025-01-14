class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count = 0
        n = len(A)
        res = [0] * n
        freqs = defaultdict(int)

        for i in range(n):
            freqs[A[i]] += 1
            if freqs[A[i]] == 2:
                count += 1
            freqs[B[i]] += 1
            if freqs[B[i]] == 2:
                count += 1
            # else: count += 1

            res[i] = count
        return res