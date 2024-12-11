class Solution:
    def maximumLength(self, s: str) -> int:
        res = -1
        cnt = {}
        def is_special(str):
            return len(set(str)) == 1

        n = len(s)
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                substring = s[i : i + length]
                if is_special(substring):
                    if substring not in cnt:
                        cnt[substring] = 1
                    else:
                        cnt[substring] += 1
                    if cnt[substring] >= 3:
                        res = max(res, length)
        
        return res    