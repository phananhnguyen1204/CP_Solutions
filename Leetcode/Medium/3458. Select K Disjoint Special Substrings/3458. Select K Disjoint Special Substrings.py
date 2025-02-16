class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        """
        k = 0
        greedy: if freq of char == 1 -> one special substring
        what if freq of char >= 1?

        keep track of first occurrence and last
        finding maximum interval can take

          [.    ]

        {            }

                1  1
        2. 2.   


        """

        first = defaultdict(int)
        last = defaultdict(int)
        n = len(s)

        for i in range(n):
            if s[i] not in first:
                first[s[i]] = i
            last[s[i]] = i

        intervals = []
        for i in range(n):
            if i != first[s[i]]: continue
            start = end = first[s[i]]
            valid = True
            for j in range(first[s[i]], last[s[i]]):
                end = max(end, last[s[j]])
                if first[s[j]] < start:
                    valid = False
                    break
            if end - start + 1 < n and valid:
                intervals.append([start, end])

        intervals.sort(key = lambda x : x[1])
        res = 0
        prev_end = -1
        for i in range(len(intervals)):
            if prev_end < intervals[i][0]:
                res += 1
                prev_end = intervals[i][1]
        print(intervals)
        return res >= k
